class TextInput:
    def __init__(self, page):
        self.page = page

    def enter_text(self, locator, text):
        self.page.locator(locator).fill(text)

    def clear_text(self, locator):
        self.page.locator(locator).fill("")
