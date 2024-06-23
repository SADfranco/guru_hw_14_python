from selene import browser, have, be


class ProfilePage:

    def open(self):
        browser.open('https://www.tsum.ru/personal/profile/')

    def check_left_menu(self, profile_menu):
        browser.all('.personal__nav-item').should(have.size(profile_menu.size))
        browser.all('.personal__nav-item').should(have.exact_texts(profile_menu.all_menu))
