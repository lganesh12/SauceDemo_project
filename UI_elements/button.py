class Button:
    def __init__(self, page):
        self.page = page

    def click_button(self, locator):
        self.page.locator(locator).click()
