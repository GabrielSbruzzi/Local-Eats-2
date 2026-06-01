# PBL 6 - Testes Unitários Automatizados e TDD

## 📚 Disciplina

Qualidade de Software

## 👨‍🎓 Aluno

Gabriel Sbruzzi

## 🎯 Objetivo

Aplicar os conceitos de Testes Unitários Automatizados utilizando Python e Pytest, seguindo a metodologia TDD (Test Driven Development).

---

# 🛠 Tecnologias Utilizadas

* Python 3.13
* Pytest

---

# 📁 Estrutura do Projeto

```text
PBL6/
├── login.py
└── test_login.py
```

---

# 🔐 Funcionalidade Escolhida

## Sistema de Login

Foi desenvolvida uma funcionalidade simples de autenticação para validar credenciais de acesso de usuários.

### Regras de Negócio

* Usuário é obrigatório.
* Senha é obrigatória.
* Credenciais válidas permitem acesso.
* Credenciais inválidas devem ser rejeitadas.

---

# 🧪 Casos de Teste Implementados

### Login com credenciais válidas

Valida se o sistema permite o acesso quando usuário e senha estão corretos.

### Login com senha inválida

Verifica se o sistema bloqueia o acesso quando a senha está incorreta.

### Usuário vazio

Valida a obrigatoriedade do preenchimento do campo usuário.

### Senha vazia

Valida a obrigatoriedade do preenchimento do campo senha.

### Usuário inexistente

Verifica se o sistema impede o acesso de usuários não cadastrados.

---

# 🔄 Aplicação do TDD

O desenvolvimento foi realizado seguindo as etapas da metodologia TDD:

## RED

Primeiramente foram criados os testes automatizados para representar os requisitos da funcionalidade.

## GREEN

Após a criação dos testes, foi implementada a lógica mínima necessária para que todos os testes fossem aprovados.

## REFACTOR

Com os testes passando, o código foi reorganizado e simplificado para melhorar sua legibilidade e manutenção sem alterar seu comportamento.

---

# 🚀 Instalação

Instale o Pytest:

```bash
pip install pytest
```

---

# ▶️ Execução dos Testes

```bash
pytest -v
```

---

# 📊 Resultado Obtido

```text
=============================
5 passed
=============================
```

Todos os cenários implementados foram executados com sucesso.

---

# 💭 Reflexão Sobre o Uso de TDD

## Foi difícil escrever testes antes do código?

Inicialmente foi um desafio, pois o desenvolvimento tradicional normalmente começa pela implementação da funcionalidade. Utilizando TDD, foi necessário analisar os requisitos e definir os cenários de teste antes de escrever o código, exigindo um planejamento maior da solução.

## O TDD ajudou no desenvolvimento?

Sim. O TDD ajudou a organizar melhor o processo de desenvolvimento, permitindo implementar pequenas partes da funcionalidade por vez e validar constantemente se os requisitos estavam sendo atendidos.

## Os testes aumentaram a confiança no código?

Sim. Os testes automatizados fornecem segurança durante alterações futuras, pois permitem verificar rapidamente se funcionalidades já implementadas continuam funcionando corretamente.

## O que melhorariam?

Seriam adicionados mais cenários de teste, incluindo casos extremos e validações adicionais. Também seria interessante ampliar a cobertura para outras funcionalidades do sistema.

## Como isso ajuda no projeto do grupo?

Os testes automatizados ajudam a identificar erros rapidamente, facilitam a integração do trabalho entre os integrantes e reduzem o risco de problemas durante a evolução do projeto. Além disso, aumentam a qualidade do software entregue e a confiança nas alterações realizadas pela equipe.

---

# 📌 Conclusão

A aplicação de Testes Unitários Automatizados e da metodologia TDD permitiu desenvolver a funcionalidade de forma organizada, segura e incremental. A prática demonstrou a importância dos testes para garantir a qualidade do software e reduzir a ocorrência de falhas durante o desenvolvimento.
