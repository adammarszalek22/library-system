from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivymd.app import MDApp

from users_functions import *

class RegisterUser(Screen):

    def register(self):
        app = MDApp.get_running_app()

        email = self.ids.email.text
        first_name = self.ids.first_name.text
        last_name = self.ids.last_name.text
        password1 = self.ids.password.text
        password2 = self.ids.password2.text

        if password1 != password2:
            self.ids.password2.error = True
            return

        if '@' not in email:
            self.ids.email.helper_text = "Your email needs to include a '@'"
            self.ids.email.error = True
            return

        reg = register_user(email, first_name, last_name, password1, password2)

        if reg == False:
            self.ids.email.helper_text = "User already exists"
            self.ids.email.error = True
            return
        
        # saving details to the app for later use
        app.email = email
        app.first_name = first_name
        app.last_name = last_name

        self.manager.current = 'MainWindow'

        self.ids.email.text = ''
        self.ids.first_name.text = ''
        self.ids.last_name.text = ''
        self.ids.password.text = ''
        self.ids.password2.text = ''

    def password(self, instance):
        # Depending on which widget calls the function
        # it will show or hide the password to the user

        if instance == self.ids.icon1:
            self.widget = self.ids.password
        else:
            self.widget = self.ids.password2

        if self.widget.password == True:
            self.widget.icon_left = "eye"
            self.widget.password = False
            Clock.schedule_once(self.focus, 0.05)
        else:
            self.widget.icon_left = "eye-off"
            self.widget.password = True
            Clock.schedule_once(self.focus, 0.05)
    
    def focus(self, dt):
        self.widget.focus = True

    def matching_passwords(self, instance):
        # 'Wrong password' error if passwords don't match
        if instance.focus == False and self.ids.password.text != instance.text:
            instance.error = True