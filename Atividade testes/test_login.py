import pytest
from login import validar_login


def test_deve_realizar_login_com_credenciais_validas():
    """
    Cenário:
    Usuário e senha corretos.

    Resultado esperado:
    True
    """

    resultado = validar_login("admin", "123456")

    assert resultado is True


def test_deve_negar_login_com_senha_incorreta():
    """
    Cenário:
    Usuário correto e senha incorreta.

    Resultado esperado:
    False
    """

    resultado = validar_login("admin", "senha_errada")

    assert resultado is False


def test_deve_gerar_erro_quando_usuario_estiver_vazio():
    """
    Cenário:
    Usuário vazio.

    Resultado esperado:
    ValueError
    """

    with pytest.raises(ValueError):
        validar_login("", "123456")


def test_deve_gerar_erro_quando_senha_estiver_vazia():
    """
    Cenário:
    Senha vazia.

    Resultado esperado:
    ValueError
    """

    with pytest.raises(ValueError):
        validar_login("admin", "")


def test_deve_negar_login_com_usuario_inexistente():
    """
    Cenário:
    Usuário não cadastrado.

    Resultado esperado:
    False
    """

    resultado = validar_login("gabriel", "123456")

    assert resultado is False