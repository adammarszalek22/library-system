from kivy.uix.screenmanager import Screen
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

from books_functions import *

class Book(Screen):
    pop_up = None

    def show_book(self, book_data):
        # book_data is in format [id, title, desc, on_loan, return_date, borrower]
        self.book_id = book_data[0]

        self.ids.img.clear_widgets()
        self.ids.name.text = ''
        self.ids.loaned_by.text = ''
        self.ids.return_date.text = ''
        self.ids.date.text = ''

        self.ids.title.text = book_data[1]
        self.ids.desc.text = book_data[2]

        if book_data[3] == "False":
            self.ids.is_available.text = "Yes"
            self.ids.button.disabled = False
        else:
            self.ids.is_available.text = "No"
            self.ids.loaned_by.text = 'Currently loaned by:'
            self.ids.name.text = str(json.loads(book_data[5])["first_name"] +
            ' ' + json.loads(book_data[5])["last_name"])
            self.ids.date.text = 'Return date:'
            self.ids.return_date.text = book_data[4][0:16]
            self.ids.button.disabled = True

        im = Image(source=f"images/img{book_data[0]}.jpg")
        self.ids.img.add_widget(im)

    def borrow_book(self):

        app = MDApp.get_running_app()
        user_details = {
            "email": app.email,
            "first_name": app.first_name,
            "last_name": app.last_name}
        self.return_date = borrow_book(user_details, self.book_id, 14)
        self.open_popup()
    
    def open_popup(self):
        app = MDApp.get_running_app()
        if self.pop_up is None:
            button = MDFlatButton(
                        text="Okay",
                        theme_text_color="Custom",
                        text_color=app.theme_cls.primary_color,
                    )
            self.pop_up = MDDialog(
                text = f"You have successfully checked out this book! " + 
                f"The return date is {self.return_date[0:16]}",
                buttons = [button]
            )
            button.bind(on_press=self.pop_up.dismiss)
        self.pop_up.text = f"You have successfully checked out this book! The return date is {self.return_date[0:16]}"
        self.pop_up.open()
    
    def clear_books(self):
        self.manager.get_screen('MainWindow').ids.box.clear_widgets()