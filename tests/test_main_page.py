import os
import allure
from allure_commons.types import Severity

from tsum_tests.pages.main_page import main_page
from tsum_tests.data.regions import Region, RegionsAll
from tsum_tests.data.items import Item
from tsum_tests.data.users import ExistingUser, NonExistingUser

@allure.tag('web')
@allure.tag('regress')
@allure.title('Change region to English')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Dropdown menu for changing regions")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_change_region_to_english():
    test_region = Region(
        region_url='english',
        region_name='English',
    )
    main_page.open()

    main_page.change_country(test_region)

    main_page.check_current_region(test_region)

@allure.tag('web')
@allure.tag('regress')
@allure.title('Change region to China')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Dropdown menu for changing regions")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_change_region_to_china():
    test_region = Region(
        region_url='chinese',
        region_name='中文',
    )
    main_page.open()

    main_page.change_country(test_region)

    main_page.check_current_region(test_region)


@allure.tag('web')
@allure.tag('regress')
@allure.title('Check all regions for choosing')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Dropdown menu for changing regions")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_all_region_for_change():
    test_region = RegionsAll(
        region_size=4,
        region_all_names=['Россия', 'عرب', 'English', '中文']
    )
    main_page.open()

    main_page.check_region_for_change(test_region)


@allure.tag('web')
@allure.tag('regress')
@allure.title('Search existing item')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Search item")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_search_item():
    test_item = Item(
        item='Джинсы'
    )
    main_page.open()

    main_page.search_item(test_item)

    main_page.check_seached_item(test_item)


@allure.tag('web')
@allure.tag('regress')
@allure.title('Login existing user by email')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Login from main page")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_login_by_email():
    test_user = ExistingUser(
        first_name='Andrew',
        last_name='Test',
        email=os.getenv("TEST_EMAIL"),
        password=os.getenv("TEST_PASSWORD"),
        phone_number='',
        bday_data='',
    )
    main_page.open()

    main_page.successful_login_by_email(test_user)

    main_page.check_successfu_login_by_email(test_user)


@allure.tag('web')
@allure.tag('regress')
@allure.title('Login non-existing user')
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Login from main page")
@allure.link("https://www.tsum.ru/", name="Main Page")
def test_login_by_non_existing_email():
    test_user = NonExistingUser(
        first_name='Andrew',
        email='andrew@yandex.ru',
        password=''
    )
    main_page.open()

    main_page.unsuccessful_login_by_non_existing_email(test_user)

    main_page.check_error_by_non_existing_email()
