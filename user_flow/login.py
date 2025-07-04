from features.locators import dict_locators


class Login:
    def __init__(self, page):
        self.page = page

    def enter_username(self, username):
        self.page.locator(dict_locators["username_text_box"]).fill(username)

    def enter_password(self, password):
        self.page.locator(dict_locators["password_text_box"]).fill(password)

    def click_login(self):
        self.page.locator(dict_locators["login_button"]).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    def is_user_logged_in(self):
        return self.page.title() == "Swag Labs"
