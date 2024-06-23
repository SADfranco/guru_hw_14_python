import os
import allure
from allure_commons.types import Severity

from tsum_tests.model.pages.main_page import MainPage
from tsum_tests.data.regions import Region, Regions_all
from tsum_tests.data.items import Item
from tsum_tests.data.users import Existing_user, Nonexisting_user

main_page = MainPage()

@allure.tag('web')
@allure.tag('regress')
@allure.title('Change region to English')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Dropdown menu for changing regions")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_change_region_to_EN():
    test_region = Region(
        region_url='english',
        region_name='English',
    )
    with allure.step("Open main page"):
        main_page.open()
    with allure.step("Change region to English"):
        main_page.change_country(test_region)
    with allure.step("Check current region after changing"):
        main_page.check_current_region(test_region)

@allure.tag('web')
@allure.tag('regress')
@allure.title('Change region to China')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Dropdown menu for changing regions")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_change_region_to_CH():
    test_region = Region(
        region_url='chinese',
        region_name='中文',
    )
    with allure.step("Open main page"):
        main_page.open()
    with allure.step("Change region to China"):
        main_page.change_country(test_region)
    with allure.step("Check current region after changing"):
        main_page.check_current_region(test_region)


@allure.tag('web')
@allure.tag('regress')
@allure.title('Check all regions for choosing')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Dropdown menu for changing regions")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_all_region_for_change():
    test_region = Regions_all(
        region_size=4,
        region_all_names=['Россия', 'عرب', 'English', '中文']
    )
    with allure.step("Open main page"):
        main_page.open()
    with allure.step("Check regions which exist for choosing"):
        main_page.check_region_for_change(test_region)


@allure.tag('web')
@allure.tag('regress')
@allure.title('Search existing item')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Searching item")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_search_item():
    test_item = Item(
        item='Джинсы'
    )
    with allure.step("Open main page"):
        main_page.open()
    with allure.step("Type item name in search filed"):
        main_page.search_item(test_item)
    with allure.step("Check page with searching results"):
        main_page.check_seached_item(test_item)


@allure.tag('web')
@allure.tag('regress')
@allure.title('Login existing user by email')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Login from main page")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_login_by_email():
    test_user = Existing_user(
        first_name='Andrew',
        last_name='Test',
        email=os.getenv("TEST_EMAIL"),
        password=os.getenv("TEST_PASSWORD"),
        phone_number='',
        bday_data='',
    )
    with allure.step("Open main page"):
        main_page.open()
    with allure.step("Login existing user"):
        main_page.successful_login_by_email(test_user)
    with allure.step("Check successful login"):
        main_page.check_successfu_login_by_email(test_user)


@allure.tag('web')
@allure.tag('regress')
@allure.title('Login nonexisting user')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Login from main page")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_login_by_nonexisting_email():
    test_user = Nonexisting_user(
        first_name='Andrew',
        email='andrew@yandex.ru',
        password=''
    )
    with allure.step("Open main page"):
        main_page.open()
    with allure.step("Login nonexisting email"):
        main_page.unsuccessful_login_by_nonexisting_email(test_user)
    with allure.step("Check error nonexisting email"):
        main_page.check_error_by_nonexisting_email()
