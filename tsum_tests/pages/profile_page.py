import allure
from selene import browser, have


class ProfilePage:

    def open(self):
        with allure.step("Open profile page"):
            browser.open('/personal/profile/')

    def check_left_menu(self, profile_menu):
        with allure.step("Check profile left menu"):
            browser.all('.personal__nav-item').should(have.size(profile_menu.size))
            browser.all('.personal__nav-item').should(have.exact_texts(profile_menu.all_menu))


profile_page = ProfilePage()
