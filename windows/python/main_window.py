from kivy.uix.screenmanager import Screen
from kivymd.uix.button import MDRectangleFlatButton

from functools import partial

from books_functions import *

class MainWindow(Screen):

    def display_books(self, instance, string):

        self.ids.box.clear_widgets()
        if string == 'all':
            books = retrieve_all()
        elif string == 'available':
            books = available()
        elif string == 'on_loan':
            books = not_available()
        else:
            books = returned_today()

        for book in books:
            if instance.text.lower() in book[1].lower():
                button = MDRectangleFlatButton(
                    text = book[1],
                    line_width = 1,
                    _line_color = (1, 1, 1, 1),
                    pos_hint = {"center_x": 0.5}
                )
                button.bind(on_press=partial(self.book_screen, book))
                self.ids.box.add_widget(button)
    
    def book_screen(self, book_info, instance):
        self.manager.get_screen('Book').show_book(book_info)
        self.manager.current = 'Book'
