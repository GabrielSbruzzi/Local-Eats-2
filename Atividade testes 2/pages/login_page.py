class LoginPage:

    URL = "https://local-eats-unisenac.vercel.app/"

    def __init__(self, page):
        self.page = page

    def acessar(self):
        self.page.goto(self.URL)

    def preencher_email(self, email):
        self.page.locator("input").nth(0).fill(email)

    def preencher_senha(self, senha):
        self.page.locator("input").nth(1).fill(senha)

    def clicar_entrar(self):
        self.page.locator("button").first.click()

    def realizar_login(self, email, senha):
        self.preencher_email(email)
        self.preencher_senha(senha)
        self.clicar_entrar()