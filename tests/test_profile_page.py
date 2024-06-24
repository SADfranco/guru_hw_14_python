import allure
from allure_commons.types import Severity
from tsum_tests.pages.profile_page import profile_page
from tsum_tests.data.menu import ProfileMenu
import tests.test_main_page as login_existing_user


@allure.tag('web')
@allure.title('Profile left menu')
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Left menu in personal profile")
@allure.link("https://www.tsum.ru/personal/profile/", name="Profile Page")
def test_profile_left_menu():
    test_data = ProfileMenu(
        size=6,
        all_menu=['Персональные данные', 'Адреса', 'Заказы', 'Карта лояльности', 'Подписки', 'Выход']
    )
    login_existing_user.test_login_by_email()

    profile_page.open()

    profile_page.check_left_menu(test_data)
