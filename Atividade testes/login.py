def validar_login(usuario, senha):
    """
    Valida credenciais de acesso.

    Regras:
    - Usuário e senha não podem estar vazios.
    - Usuário deve ser 'admin'.
    - Senha deve ser '123456'.
    """

    usuario_correto = "admin"
    senha_correta = "123456"

    if not usuario or not senha:
        raise ValueError("Usuário e senha são obrigatórios")

    return usuario == usuario_correto and senha == senha_correta