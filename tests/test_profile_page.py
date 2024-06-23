import allure
from allure_commons.types import Severity
from tsum_tests.model.pages.profile_page import ProfilePage
from tsum_tests.data.menu import Profile_menu
import tests.test_main_page as login_existing_user

profile_page = ProfilePage()

@allure.tag('web')
@allure.title('Profile left menu')
@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "SADfranco")
@allure.feature("Left menu in personal profile")
@allure.link("https://www.tsum.ru/personal/profile/", name="Profile Page")
def test_profile_left_menu():
    test_data = Profile_menu(
        size=6,
        all_menu=['Персональные данные', 'Адреса', 'Заказы', 'Карта лояльности', 'Подписки', 'Выход']
    )
    with allure.step("Login existing user"):
        login_existing_user.test_login_by_email()
    with allure.step("Open profile page"):
        profile_page.open()
    with allure.step("Check profile left menu"):
        profile_page.check_left_menu(test_data)


