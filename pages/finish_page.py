from pages.base_page import BasePage
from pages.locators import FinishPageLocators


class FinishPage(BasePage):
    def should_finish_page(self):
        self.should_present_form_finish_page()
        self.should_present_button_back_home()

    def should_present_form_finish_page(self):
        assert self.is_element_present(*FinishPageLocators.FINISH_PAGE_FORM), 'Not form finish page'

    def should_present_button_back_home(self):
        assert self.is_element_present(*FinishPageLocators.BUTTON_BACK_HOME), 'Not button back home'
