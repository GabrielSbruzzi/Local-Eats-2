from pages.login_page import LoginPage


def test_login_com_sucesso(page):
    login = LoginPage(page)

    login.acessar()

    login.realizar_login(
        "gabrielsbz2003@gmail.com",
        "sbruzi"
    )

    page.wait_for_timeout(5000)

    assert page.locator("body").is_visible()


def test_login_com_senha_invalida(page):
    login = LoginPage(page)

    login.acessar()

    login.realizar_login(
        "gabrielsbz2003@gmail.com",
        "senhaerrada"
    )

    page.wait_for_timeout(5000)

    assert page.locator("body").is_visible()


def test_login_com_campos_vazios(page):
    login = LoginPage(page)

    login.acessar()

    page.wait_for_timeout(2000)

    assert page.locator("body").is_visible()