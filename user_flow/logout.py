from features.locators import dict_locators


class Logout:
    def __init__(self, page):
        self.page = page

    def logout(self):
        self.page.locator(dict_locators["open_menu"]).click()
        self.page.locator(dict_locators["logout"]).click()

