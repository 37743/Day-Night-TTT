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
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from scripts.ttt import (BOARD_X,BOARD_Y,BOARD_DIMENSIONS,MARK_X,state)
from scripts.ttt import TTT
from functools import partial
import sqlauth

ROW_HEIGHT = 100
COL_WIDTH = 100
SPACING_X = 10
SPACING_Y = 10

Window.size = (400, 500)

def reSize(*args):
   Window.size = (400, 500)
   return True

Window.bind(on_resize = reSize)
# New board
board = TTT()
move_history = ""

def insert_record(match_winner, match_history):
    ''' Inserts match results as a new entry to the SQL server'''
    sql = "INSERT INTO matches (date, p1_id, p2_id, match_winner, match_history) VALUES (CURRENT_TIMESTAMP, %s, %s, %s, %s)"
    val = (1, 2, match_winner, match_history)
    cursor = sqlauth.tttdb.cursor()
    cursor.execute(sql, val)
    sqlauth.tttdb.commit()

def export_to_csv(filename="matches"):
    ''' Export matches table from the database into a comma separated file'''
    cursor = sqlauth.tttdb.cursor()
    cursor.execute("SELECT * FROM matches INTO OUTFILE '{f}.csv';".format(f=filename))
    sqlauth.tttdb.commit()

def back_released(instance):
    App.get_running_app().screen_manager.current = "Main Menu"

# General purpose cell press button
def cell_pressed(instance, move, cell):
    ''' Button that does a series of operations that evaluates
    the current state of the match'''
    cell.background_disabled_normal = "assets/x-cell.png"\
        if board.get_player() == MARK_X else "assets/o-cell.png"
    cell.background_disabled_down = "assets/x-cell-50.png"\
        if board.get_player() == MARK_X else "assets/o-cell-50.png"
    # print("TURN = {t}, MOVE = {m}, PLAYER = {p}".format(t=board.get_turn(),m=move,p=board.get_player()))
    global move_history
    move_history = move_history + "{t}. P{p}".format(t=board.get_turn(), p=board.get_player()) + ":C{c} ".format(c=move)
    board.play(move)
    cell.disabled = True
    if board.get_result() != 3:
        result = list(state.keys())[list(state.values()).index(board.get_result())]
        game_status.text = "Game Status: {s}".format(s=result)
        for widget in cells:
            widget.disabled = True
        insert_record(board.get_result(), move_history)

# Creating all 9 buttons
# TODO: RESET ALL ENTRIES AND THE MATRIX TO ALLOW REMATCHES
cells = np.array([Button(background_normal = "assets/empty-cell.png",
             background_disabled_normal = "assets/empty-cell.png")\
                for i in range(9)])

for i, obj in enumerate(cells):
    obj.bind(on_press=partial(cell_pressed, cell=obj, move=i))

    
cells_2d = cells.reshape(BOARD_DIMENSIONS)

game_status = Label(text = "Game Status: {s}".format(s='NOT_OVER'), color = (1,1,1), bold = True,
                                 outline_width = 2.5, outline_color = (0.1,0.1,0.1),
                                 font_size = 14, pos = (0,200))

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
        self.ttt_grid = GridLayout(row_force_default = True, row_default_height = ROW_HEIGHT,
                                   col_force_default = True, col_default_width = COL_WIDTH,
                                   rows = BOARD_X, cols = BOARD_Y,
                                   spacing = [SPACING_X,SPACING_Y], pos = ((COL_WIDTH+SPACING_X*(BOARD_X-1))/BOARD_X, -120))
        for widget in cells:
            self.ttt_grid.add_widget(widget)
        self.add_widget(self.ttt_grid)

        # Back button
        self.back_to_menu = Button(background_normal = "assets/back-icon.png",
                                    background_down = "assets/back-icon-down.png",
                                    pos_hint={"center_x": 0.1, "center_y": .92},
                                    size_hint=(None,None),
                                    size=(65,63))
        self.back_to_menu.bind(on_release=back_released)
        self.add_widget(self.back_to_menu)
