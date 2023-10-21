# Yousef (Ibrahim) Gomaa - ID: 320210207
# Egypt-Japan University of Science and Technology
# Artificial Intelligence and Data Science Department
# Tic-Tac-Toe Main Launcher
# ---
import kivy
kivy.require('2.2.0')

from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, WipeTransition
import scripts.screens.pvp as PVPPage
import scripts.screens.menu as MenuPage
import scripts.screens.pva as PVAPage
from config import settings

class App(App):
    def build(self):
        self.title = settings.VersionInfo.get_title()
        self.icon = "assets/logo.png"
        self.menu = MenuPage.Menu(name="Main Menu")
        self.pvp = PVPPage.Game(name="Player VS Player")
        self.pva = PVAPage.Game(name="Player VS AI")
        # PVPPage.export_to_csv()
        self.screen_manager = ScreenManager(transition = WipeTransition())

        for screen in [self.menu, self.pvp, self.pva]:
            self.screen_manager.add_widget(screen)
        return self.screen_manager

if __name__ == '__main__':  
    main = App()
    main.run()
