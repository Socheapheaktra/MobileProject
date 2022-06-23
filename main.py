from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.app import MDApp

class MainWindow(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def change_screen(self):
        self.ids.scrn_mngr.current = "scrn_2" if self.ids.scrn_mngr.current == "scrn_1" else "scrn_1"

class MainApp(MDApp):
    def build(self):
        return MainWindow()

if __name__ == '__main__':
    MainApp().run()