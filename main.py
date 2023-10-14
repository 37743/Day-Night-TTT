# Yousef (Ibrahim) Gomaa - ID: 320210207
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Tic-Tac-Toe Main Launcher
# ---
import kivy
kivy.require('2.2.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, FadeTransition
import scripts.screens.pvp as PVPPage
from config import settings

class App(App):
    def build(self):
        self.title = settings.VersionInfo.get_title()
        self.icon = "assets/project-TTT-icon.png"
        self.pvp = PVPPage.Game(name="Player VS Player")
        # PVPPage.export_to_csv()
        self.screen_manager = ScreenManager(transition = FadeTransition())

        for screen in [self.pvp]:
            self.screen_manager.add_widget(screen)
        return self.screen_manager

if __name__ == '__main__':  
    main = App()
    main.run()
