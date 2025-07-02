from UI_elements.button import Button
from UI_elements.TextInput import TextInput
from user_flow.login import Login
from user_flow.logout import Logout


class User:
    def __init__(self, page, context, username, password):
        self.page = page
        self.context = context
        self.username = username
        self.password = password

    def login(self):
        Login(self.page).login(self.username, self.password)

    def logout(self):
        Logout(self.page).logout()

    def enter_text(self, locator, text):
        TextInput(self.page).enter_text(locator, text)

    def click_btn(self, locator):
        Button(self.page).click_button(locator)

    def is_user_logged_in(self):
        return Login(self.page).is_user_logged_in()
