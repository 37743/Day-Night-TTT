# Yousef (Ibrahim) Gomaa - ID: 320210207
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Tic-Tac-Toe Menu
# ---
# --------
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
# from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.animation import Animation
# from kivy.clock import Clock

def button_swipe(widget):
    anim = Animation(pos=(800, 250), duration=2, t='in_cubic')
    anim.start(widget)
    return

def float_effect(widget, yn, d):
    anim = Animation(y=-yn, duration = d, t="in_out_cubic") + Animation(y=0, duration=d, t="in_out_cubic")
    anim.repeat = True
    anim.start(widget)
    return

def pvp_released(instance):
    # button_swipe(instance)
    # Clock.schedule_once(change_to_screen, 2)
    change_to_screen(screen="Player VS Player")
    return

def pva_released(instance):
    # button_swipe(instance)
    # Clock.schedule_once(change_to_screen, 2)
    change_to_screen(screen="Player VS AI")
    return 

def change_to_screen(*args, screen):
    App.get_running_app().screen_manager.current = screen
    return

class Menu(Screen, FloatLayout):
    def _update_bg(self, instance, value):
        self.bg.pos = instance.pos
        self.bg.size = instance.size

    def __init__(self, **kwargs):
        super(Menu, self).__init__(**kwargs)
        with self.canvas.before:
            self.bg = Rectangle(source = "assets/menu-bg-sky.png",
                                size = self.size,
                                pos = self.pos)

        self.bind(size = self._update_bg, pos = self._update_bg)

        # Parallax Background Collection
        bgnames = ['sun','cloudsback','cloudsfront',
                   'mountains1','mountains2','mountains3',
                   'lake','trees1','trees2',
                   'trees3','trees4','gradient']
        
        floatvalues = [[-10,4],[0,0],[0,0],
                       [9,7],[10,6],[11,5],
                       [12,4],[13,4],[14,4],
                       [11,4],[14,3],[0,0]]

        bgfloat = [FloatLayout() for i in range(12)]

        bg = [Image(source = "assets/menu-bg-{t}.png".format(t=i),
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})\
                        for i in bgnames]

        for i,obj in enumerate(bg):
            bgfloat[i].add_widget(obj)
            float_effect(bgfloat[i], floatvalues[i][0], floatvalues[i][1])

        # Game Logo
        self.floatbox = FloatLayout()
        self.logo = Image(source="assets/logo.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .87})
        self.floatbox.add_widget(self.logo)
        # Text Logo
        self.dlogo = Image(source="assets/subtitle.png",
                    size_hint = (.5,.5),
                    pos_hint={"center_x": .5, "center_y": .73})
        self.floatbox.add_widget(self.dlogo)
        
        float_effect(self.floatbox, 10, 2)
        self.add_widget(self.floatbox)

        for widget in bgfloat:
            self.add_widget(widget)

        # Button Vertical Box
        self.buttonbox = BoxLayout(orientation = 'vertical',
                                   spacing = 10,
                                   size_hint=(1,.3),
                                   pos_hint={"center_x": .75, "center_y": .4})
        
        # Play (PVP) Button
        pvpbut = Button(text="Player VS Player", color = "#f5f7f8",
                             outline_width=2, outline_color ="#3c808b",
                            size_hint=(.5,.4), font_size=18,
                            background_normal=
                            "assets/button2.png",
                            background_down=
                            "assets/button-down2.png")
        pvpbut.bind(on_release=pvp_released)
        self.buttonbox.add_widget(pvpbut)

        # Play (A.I.) Button
        pvabut = Button(text="Player VS A.I.", color = "#f5f7f8",
                             outline_width=2, outline_color ="#3c808b",
                            size_hint=(.5,.4), font_size=18,
                            background_normal=
                            "assets/button2.png",
                            background_down=
                            "assets/button-down2.png")
        #
        pvabut.bind(on_release=pva_released)
        self.buttonbox.add_widget(pvabut)
        
        # Leaderboard
        lbbut = Button(text="Leaderboard", color = "#f5f7f8",
                             outline_width=2, outline_color ="#3c808b",
                            size_hint=(.5,.4), font_size=18,
                            background_normal=
                            "assets/button2.png",
                            background_down=
                            "assets/button-down2.png")
        #
        self.buttonbox.add_widget(lbbut)

        self.add_widget(self.buttonbox)

        # Footer
        self.footer = Label(text="\"tictactoe\" - @github.com/37743",
                             color = "#f5f7f8",
                             outline_width=1, outline_color = "#3c808b",
                             pos_hint={"center_x": .5, "center_y": .04}, font_size=11)
        #
        self.add_widget(self.footer)