# Yousef (Ibrahim) Gomaa - ID: 320210207
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Tic-Tac-Toe Player VS Player
# ---
import numpy as np
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from scripts.ttt import (BOARD_X,BOARD_Y,BOARD_DIMENSIONS,state)
from scripts.ttt import TTT
from functools import partial
# import sqlauth

ROW_HEIGHT = 100
COL_WIDTH = 100
SPACING_X = 10
SPACING_Y = 10
TYPE = 'RND'

Window.size = (400, 500)

def reSize(*args):
   Window.size = (400, 500)
   return True

Window.bind(on_resize = reSize)
# New board
boardai = TTT()
move_history_pva = ""

# def insert_record(match_winner, match_history):
#     ''' Inserts match results as a new entry to the SQL server'''
#     sql = "INSERT INTO matches (date, p1_id, p2_id, match_winner, match_history) VALUES (CURRENT_TIMESTAMP, %s, %s, %s, %s)"
#     val = (1, 2, match_winner, match_history)
#     cursor = sqlauth.tttdb.cursor()
#     cursor.execute(sql, val)
#     sqlauth.tttdb.commit()

# def export_to_csv(filename="matches"):
#     ''' Export matches table from the database into a comma separated file'''
#     cursor = sqlauth.tttdb.cursor()
#     cursor.execute("SELECT * FROM matches INTO OUTFILE '{f}.csv';".format(f=filename))
#     sqlauth.tttdb.commit()

def back_released(instance):
    ''' Back button method that moves the user to the main menu when called'''
    App.get_running_app().screen_manager.current = "Main Menu"

# General purpose cell press button
def cell_pressed(instance, move, cell):
    ''' Button that does a series of operations that evaluates the current state of the match'''
    boardai.play(move, pvp=False)
    cell.background_disabled_normal = "assets/x-cell.png"
    cell.background_disabled_down = "assets/x-cell-50.png"
    global move_history_pva
    move_history_pva = move_history_pva + "{t}. P{p}".format(t=boardai.get_turn(pvp=False),\
                            p=boardai.get_player(pvp=False)) + ":C{c} ".format(c=move)
    cell.disabled = True
    # A.I. plays if game has not ended.
    if not(check_results(boardai, cells, move_history_pva)):
        ai_cell_pressed(board=boardai, cells=cells)

def ai_cell_pressed(board, cells):
    ''' A.I. plays their move on the GUI'''
    board.play_ai(TYPE)
    cell = board.get_ai_cell()
    cells[cell].background_disabled_normal = "assets/o-cell.png"
    cells[cell].background_disabled_down = "assets/o-cell-50.png"
    global move_history_pva
    move_history_pva = move_history_pva + "{t}. P{p}".format(t=boardai.get_turn(pvp=False),\
                            p=boardai.get_player(pvp=False)) + ":C{c} ".format(c=cell)
    cells[cell].disabled = True
    check_results(board, cells, move_history_pva)


def check_results(boardai, cells, move_history_pva):
    ''' Returns True if game has ended and calls the send results method to the SQL server'''
    if boardai.get_result() != 3:
        result = list(state.keys())[list(state.values()).index(boardai.get_result())]
        game_status.text = "Game Status: {s}!".format(s=str(result))
        for widget in cells:
            widget.disabled = True
        # insert_record(boardai.get_result(), move_history_pva)
        return True
    return False

def reset_released(instance, grid):
    ''' Resets the widgets on board back to empty cells'''
    print("\nRESET PRESSED!\n")
    boardai.reset(pvp=False)
    grid_iter = [i for i in grid.children]
    for widget in grid_iter:
        widget.background_normal = "assets/empty-cell.png"
        widget.background_disabled_normal = "assets/empty-cell.png"
        widget.disabled = False
    game_status.text = "Game Status: {s}!".format(s="ONGOING")
    global move_history_pva
    move_history_pva = ""

def type_released(instance, type, grid):
    global TYPE
    TYPE = type
    ai_solve_mode.text = "Mode: {s}!".format(s=TYPE)
    print('\n' + type + " PRESSED!")
    reset_released(instance, grid)
    return

# Creating all 9 buttons
cells = np.array([Button(background_normal = "assets/empty-cell.png",
             background_disabled_normal = "assets/empty-cell.png")\
                for i in range(9)])

for i, obj in enumerate(cells):
    obj.bind(on_press=partial(cell_pressed, cell=obj, move=i))

    
cells_2d = cells.reshape(BOARD_DIMENSIONS)

game_status = Label(text = "Game Status: {s}!".format(s="ONGOING"), color = "#f5f7f8",
                                 bold = True, outline_width = 2.5, outline_color = "#3c808b",
                                 font_size = 18, pos = (0,210))

ai_solve_mode = Label(text = "Mode: {s}!".format(s=TYPE), color = "#f5f7f8",
                                 bold = True, outline_width = 2.5, outline_color = "#3c808b",
                                 font_size = 18, pos = (0,230))
class Game(Screen, FloatLayout):
    def _update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        with self.canvas.before:
            self.bg = Rectangle(source = "assets/menu-bg.png",
                                size = self.size,
                                pos = self.pos)

        self.bind(size = self._update_bg, pos = self._update_bg)
        # Widgets
        self.grid_bg = Image(source = "assets/grid-bg.png",
                                 size=self.size,
                                 pos=(0,-30))
        self.add_widget(self.grid_bg)
        self.add_widget(game_status)
        self.add_widget(ai_solve_mode)
        self.ttt_grid = GridLayout(row_force_default = True, row_default_height = ROW_HEIGHT,
                                col_force_default = True, col_default_width = COL_WIDTH,
                                rows = BOARD_X, cols = BOARD_Y,
                                spacing = [SPACING_X,SPACING_Y],
                                pos = ((COL_WIDTH+SPACING_X*(BOARD_X-1))/BOARD_X, -120))

        for widget in cells:
            self.ttt_grid.add_widget(widget)
        self.add_widget(self.ttt_grid)

        # Back button
        self.backbut = Button(background_normal = "assets/back-icon.png",
                                    background_down = "assets/back-icon-down.png",
                                    pos_hint={"center_x": 0.1, "center_y": .92},
                                    size_hint=(None,None),
                                    size=(57,56))
        self.backbut.bind(on_release=back_released)
        self.add_widget(self.backbut)

        # Reset button
        self.resetbut = Button(background_normal = "assets/reset-icon.png",
                                background_down = "assets/reset-icon-down.png",
                                pos_hint={"center_x": 0.9, "center_y": .92},
                                size_hint=(None,None),
                                size=(57,56))
        
        self.resetbut.bind(on_release=lambda instance:\
                            reset_released(instance, self.ttt_grid))
        self.add_widget(self.resetbut)       

        # Type button(s)
        buts = np.array([Button(text=type, color = "#f5f7f8",
                            outline_width=2, outline_color ="#3c808b",
                            background_normal = "assets/button-icon.png",
                            background_down = "assets/button-icon-down.png",
                            size_hint=(None,None),
                            size=(57,56))\
                for type in ['RND','DFS','BFS','UCS','GS']])

        for obj in buts:
            obj.bind(on_release=partial(type_released, type=obj.text, grid=self.ttt_grid))

        self.typebox = BoxLayout(orientation='horizontal',
                                 size_hint=(1,1),
                                 size=(400,56),
                                 pos_hint={"center_x": .645, "center_y": 0.5})
        for widget in buts:
            self.typebox.add_widget(widget)

        self.add_widget(self.typebox)