from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from kivymd.app import MDApp

from users_functions import *

class Login(Screen):

    def login(self):

        app = MDApp.get_running_app()

        email = self.ids.email.text
        password = self.ids.password.text

        user = find_user(email)

        if not user:
            self.ids.email.helper_text = "User doesn't exist"
            self.ids.email.error = True
            return
        
        try_login = login_user(email, password)

        if not try_login:
            self.ids.password.helper_text = "Wrong password"
            self.ids.password.error = True
            return

        # saving details to the app for later use
        app.email = email
        app.first_name = user[1]
        app.last_name = user[2]

        self.manager.current = "MainWindow"     

        self.ids.email.text = ''
        self.ids.password.text = ''

    def password(self, instance):
        # This will show or hide the password to the user
        self.widget = self.ids.password

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