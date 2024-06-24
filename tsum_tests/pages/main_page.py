import allure
from selene import browser, have, be


class MainPage:

    def open(self):
        with allure.step("Open main page"):
            browser.open('/')

    def check_region_for_change(self, regions_all):
        with allure.step("Change region to English"):
            browser.element('[data-test-id="regionPickerButton"]').should(be.clickable).click()
            browser.element('.RegionPicker__content___ZCHL1').all('[data-test-id="selectRegionName"]').should(
                have.size(regions_all.region_size))
            browser.element('.RegionPicker__content___ZCHL1').all('[data-test-id="selectRegionName"]').should(
                have.exact_texts(regions_all.region_all_names))

    def check_current_region(self, region):
        with allure.step("Check current region"):
            browser.element('[data-test-id="currentRegionName"]').should(have.exact_text(region.region_name))
            browser.should(have.url(f'https://www.tsum.ru/{region.region_url}/'))

    def change_country(self, region):
        with allure.step("Change region to another"):
            browser.element('[data-test-id="regionPickerButton"]').should(be.clickable).click()
            browser.all('[data-test-id="selectRegionName"]').element_by(have.exact_text(region.region_name)).click()

    def search_item(self, item):
        with allure.step("Type searching item amd press"):
            browser.element('[placeholder="Поиск"]').type(item.item).press_enter()

    def check_seached_item(self, item):
        with allure.step("Check searched item"):
            browser.element('[data-test-id="catalogTitle"]').should(have.exact_text(f'Поиск: {item.item}'.upper()))
            browser.element('[data-test-id="currentCatalog"]').should(have.text(f'Поиск: {item.item}'))

    def successful_login_by_email(self, existing_user):
        with allure.step("Fill email and password"):
            browser.element('[data-test-id="buttonLogin"]').click()
            browser.element('[data-test-id="loginViaEmail"]').click()
            browser.element('[placeholder="Ваш email"]').type(existing_user.email)
            browser.element('[type="password"]').type(existing_user.password)

    def check_successfu_login_by_email(self, existing_user):
        with allure.step("Check successful login by email"):
            browser.should(have.url('https://www.tsum.ru/'))
            browser.element('[data-test-id="userProfile"]').should(
                have.exact_text(existing_user.first_name + ' ' + existing_user.last_name))

    def unsuccessful_login_by_non_existing_email(self, non_existing_user):
        with allure.step("Fill non-existing email"):
            browser.element('[data-test-id="buttonLogin"]').click()
            browser.element('[data-test-id="loginViaEmail"]').click()
            browser.element('[placeholder="Ваш email"]').type(non_existing_user.email)

    def check_error_by_non_existing_email(self):
        with allure.step("Check error unsuccessful login by non-existing email"):
            browser.element('[data-test-id="emailInputBlockWrapper"]').should(have.exact_text('Клиент не найден'))


main_page = MainPage()
