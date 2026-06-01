# PBL 7 - Testes Funcionais Automatizados

## 📚 Disciplina

Qualidade de Software

## 👨‍🎓 Aluno

Gabriel Sbruzzi

## 🎯 Objetivo

Automatizar fluxos funcionais da aplicação LocalEats utilizando Playwright, Pytest e o padrão Page Object Model (POM), aplicando conceitos de automação de testes de interface.

---

# 🔐 Fluxo Funcional Escolhido

## Login de Usuário

O fluxo automatizado foi o processo de autenticação do usuário no sistema LocalEats.

Este fluxo foi escolhido por ser uma funcionalidade crítica da aplicação, pois é o ponto de entrada para acesso às demais funcionalidades do sistema.

---

# 🛠 Tecnologias Utilizadas

* Python 3.13
* Playwright
* Pytest
* Pytest-Playwright

---

# 📁 Estrutura do Projeto

```text
PBL7/
├── pages/
│   └── login_page.py
│
├── tests/
│   └── test_login.py
│
└── pytest.ini
```

---

# 🧪 Cenários Automatizados

## Login com sucesso

Valida o acesso ao sistema utilizando credenciais válidas.

## Login com senha inválida

Verifica o comportamento da aplicação quando uma senha incorreta é informada.

## Login com campos vazios

Valida o comportamento do sistema quando o usuário tenta realizar login sem preencher os campos obrigatórios.

---

# 🤖 Utilização do Playwright Codegen

Para auxiliar na criação dos testes foi utilizado o recurso Codegen do Playwright.

### Comando utilizado

```bash
playwright codegen https://local-eats-unisenac.vercel.app/
```

### Benefícios observados

* Identificação rápida dos elementos da página.
* Geração automática de ações do usuário.
* Redução do tempo necessário para iniciar a automação.

### Ajustes realizados

Após a geração inicial, foi necessário organizar o código utilizando o padrão Page Object Model para melhorar a manutenção e reutilização.

---

# 🏗 Aplicação do Page Object Model (POM)

Foi utilizado o padrão POM para separar os elementos da interface dos casos de teste.

### Benefícios obtidos

* Melhor organização do código.
* Reutilização de métodos.
* Facilidade de manutenção.
* Redução da duplicação de código.

---

# 🚀 Instalação

Instalação das dependências:

```bash
pip install pytest
pip install playwright
pip install pytest-playwright
```

Instalação dos navegadores:

```bash
playwright install
```

---

# ▶️ Execução dos Testes

```bash
pytest -v --headed
```

---

# 📊 Resultado Obtido

```text
=============================
3 passed
=============================
```

Todos os cenários automatizados foram executados com sucesso.

---

# 💭 Reflexão Sobre a Automação de Testes

## Foi difícil escrever os testes?

A principal dificuldade foi identificar os seletores corretos dos elementos da interface e configurar corretamente o ambiente do Playwright. Após a configuração inicial, a criação dos testes tornou-se mais simples e organizada.

## A automação ajudou no desenvolvimento?

Sim. A automação permitiu executar rapidamente os mesmos cenários diversas vezes, reduzindo o esforço manual e aumentando a produtividade durante as validações.

## Os testes aumentaram a confiança no sistema?

Sim. Os testes automatizados ajudam a verificar rapidamente se funcionalidades importantes continuam funcionando após alterações na aplicação, reduzindo o risco de regressões.

## O que melhorariam?

Seriam automatizados outros fluxos importantes do sistema, além da melhoria dos seletores e da criação de uma massa de dados específica para testes automatizados.

## Como isso ajuda no projeto do grupo?

A automação reduz o tempo gasto com testes manuais, aumenta a qualidade das entregas e permite que a equipe identifique problemas mais rapidamente. Isso facilita a colaboração entre os integrantes e torna o processo de desenvolvimento mais seguro e eficiente.

---

# 📌 Conclusão

A utilização do Playwright juntamente com Pytest e o padrão Page Object Model permitiu criar testes funcionais automatizados de forma organizada e reutilizável. A automação contribui para aumentar a qualidade do software, reduzir erros e agilizar as validações durante o desenvolvimento do projeto.
