from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.screenmanager import NoTransition

from windows.python.register_user import RegisterUser
from windows.python.login import Login
from windows.python.main_window import MainWindow
from windows.python.book import Book

from books_functions import on_start_up

class WindowManager(ScreenManager):
    pass

class AwesomeApp(MDApp):
    def build(self):
        on_start_up()
        kv = Builder.load_file('kivy.kv')
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = 'Green'
        WindowManager.transition = NoTransition()
        return kv

if __name__ == '__main__':
    AwesomeApp().run()