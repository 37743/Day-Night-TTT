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
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.graphics import Rectangle
from kivy.animation import Animation
from kivy.clock import Clock

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
    # Clock.schedule_once(change_to_pvp, 2)
    change_to_pvp()
    return 

def change_to_pvp(*args):
    App.get_running_app().screen_manager.current = "Player VS Player"
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
        bgsun = Image(source = "assets/menu-bg-sun.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})
        self.floatbg1 = FloatLayout()
        self.floatbg1.add_widget(bgsun)
        float_effect(self.floatbg1, -10, 4)

        self.floatbg2 = FloatLayout()
        bgcb = Image(source = "assets/menu-bg-cloudsback.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})
        self.floatbg2.add_widget(bgcb)
        # float_effect(self.floatbg2, 7, 8)

        self.floatbg3 = FloatLayout()
        bgcf = Image(source = "assets/menu-bg-cloudsfront.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})
        self.floatbg3.add_widget(bgcf)
        # float_effect(self.floatbg3, 8, 8)

        self.floatbg4 = FloatLayout()
        bgm1 = Image(source = "assets/menu-bg-mountains1.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})
        self.floatbg4.add_widget(bgm1)
        float_effect(self.floatbg4, 9, 7)

        bgm2 = Image(source = "assets/menu-bg-mountains2.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})
        self.floatbg5 = FloatLayout()
        self.floatbg5.add_widget(bgm2)
        float_effect(self.floatbg5, 10, 6)

        self.floatbg6 = FloatLayout()
        bgm3 = Image(source = "assets/menu-bg-mountains3.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})
        self.floatbg6.add_widget(bgm3)
        float_effect(self.floatbg6, 11, 5)

        self.floatbg7 = FloatLayout()
        bglk = Image(source = "assets/menu-bg-lake.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})
        self.floatbg7.add_widget(bglk)
        float_effect(self.floatbg7, 12, 4)

        self.floatbg8 = FloatLayout()
        bgt1 = Image(source = "assets/menu-bg-trees1.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})
        self.floatbg8.add_widget(bgt1)
        float_effect(self.floatbg8, 13, 4)

        self.floatbg9 = FloatLayout()
        bgt2 = Image(source = "assets/menu-bg-trees2.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})
        self.floatbg9.add_widget(bgt2)
        float_effect(self.floatbg9, 14, 4)

        self.floatbg10 = FloatLayout() 
        bgt3 = Image(source = "assets/menu-bg-trees3.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})
        self.floatbg10.add_widget(bgt3)
        float_effect(self.floatbg10, 11, 4)

        self.floatbg11 = FloatLayout() 
        bgt4 = Image(source = "assets/menu-bg-trees4.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})
        self.floatbg11.add_widget(bgt4)
        float_effect(self.floatbg11, 14, 3)

        bggd = Image(source = "assets/menu-bg-gradient.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .5})
        self.add_widget(bggd)

        # Game Logo
        self.logo = Image(source="assets/logo.png",
                            size_hint = (1,1),
                            pos_hint={"center_x": .5, "center_y": .87})
        # Text Logo
        self.dlogo = Image(source="assets/subtitle.png",
                    size_hint = (.5,.5),
                    pos_hint={"center_x": .5, "center_y": .73})
        self.floatbox = FloatLayout()
        self.floatbox.add_widget(self.logo)
        self.floatbox.add_widget(self.dlogo)
        float_effect(self.floatbox, 10, 2)
        for widget in [self.floatbg1,self.floatbg2,self.floatbg3,
                       self.floatbg4,self.floatbg5,self.floatbg6,
                       self.floatbg7,self.floatbg8,self.floatbg9,
                       self.floatbg10,self.floatbg11,self.floatbox]:
            self.add_widget(widget)
        # Play (PVP) Button
        pvpbut = Button(text="Player VS Player", color = "#f5f7f8",
                             outline_width=2, outline_color ="#3c808b",
                            size_hint=(.5,.1), font_size=20,
                            background_normal=
                            "assets/button2.png",
                            background_down=
                            "assets/button-down2.png")
        pvpbut.bind(on_release=pvp_released)
        # Play (A.I.) Button
        pvabut = Button(text="Player VS A.I.", color = "#f5f7f8",
                             outline_width=2, outline_color ="#3c808b",
                            size_hint=(.5,.1), font_size=20,
                            background_normal=
                            "assets/button2.png",
                            background_down=
                            "assets/button-down2.png")
        lbbut = Button(text="Leaderboard", color = "#f5f7f8",
                             outline_width=2, outline_color ="#3c808b",
                            size_hint=(.5,.1), font_size=20,
                            background_normal=
                            "assets/button2.png",
                            background_down=
                            "assets/button-down2.png")
        self.buttonbox = BoxLayout(orientation = 'vertical',
                                   spacing = 10,
                                   size_hint=(1,.25),
                                   pos_hint={"center_x": .75, "center_y": .4})
        self.buttonbox.add_widget(pvpbut)
        self.buttonbox.add_widget(pvabut)
        self.buttonbox.add_widget(lbbut)

        self.add_widget(self.buttonbox)

        # Footer
        self.footer = Label(text="\"tictactoe\" - @github.com/37743",
                             color = "#f5f7f8",
                             outline_width=1, outline_color = "#3c808b",
                             pos_hint={"center_x": .5, "center_y": .04}, font_size=11)
        self.add_widget(self.footer)