class BasePage:
    """Trusa de scule comună pentru toate paginile."""

    def __init__(self, page):
        self.page = page

    def deschide(self, path="/"):
        self.page.goto(path)
