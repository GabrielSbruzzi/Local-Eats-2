from pytest_bdd import scenarios, given, when, then

scenarios("../features/navegacao.feature")


@given("que o usuário acessa o LocalEats")
def acessar(page):
    page.goto("https://local-eats-unisenac.vercel.app/")


@when("a página carregar completamente")
def carregar(page):
    page.wait_for_load_state("networkidle")


@then("o sistema deve exibir uma página válida")
def validar_pagina(page):
    assert page.url is not None
    assert "local-eats" in page.url


@then("o título da página deve estar preenchido")
def validar_titulo(page):
    assert page.title() != ""