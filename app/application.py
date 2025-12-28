from pages.left_panel import LeftPanel
from pages.simple_registration_page import SimpleRegistrationPage


class Application:
    def __init__(self):
        self.left_panel = LeftPanel()
        self.simple_registration_form = SimpleRegistrationPage()
