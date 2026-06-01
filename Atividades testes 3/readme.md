# PBL 8 - BDD e Automação Orientada a Comportamento

## Integrante

Gabriel Sbruzzi

## Objetivo

Aplicar os conceitos de Behavior-Driven Development (BDD) utilizando Python, pytest-bdd e Playwright para transformar comportamentos do sistema LocalEats em cenários automatizados e legíveis para equipes técnicas e não técnicas.

## Tecnologias Utilizadas

* Python 3.13
* Pytest
* Pytest-BDD
* Playwright
* VS Code

## Estrutura do Projeto

```text
projeto/
│
├── features/
│   └── navegacao.feature
│
├── tests/
│   └── test_navegacao.py
│
└── README.md
```

## Fluxo Escolhido

### Navegação entre páginas

Este fluxo valida o comportamento básico de navegação do sistema LocalEats, garantindo que o usuário consiga acessar a aplicação corretamente e visualizar suas informações principais.

## Cenários BDD

### Cenário 1 - Acessar página inicial

```gherkin
Scenario: Acessar página inicial
    Given que o usuário acessa o LocalEats
    When a página carregar completamente
    Then o sistema deve exibir uma página válida
```

### Cenário 2 - Verificar título da página

```gherkin
Scenario: Verificar título da página
    Given que o usuário acessa o LocalEats
    When a página carregar completamente
    Then o título da página deve estar preenchido
```

## Instalação

Instalar as dependências:

```bash
pip install pytest pytest-bdd playwright pytest-playwright
```

Instalar os navegadores do Playwright:

```bash
playwright install
```

## Execução dos Testes

Executar todos os cenários:

```bash
python -m pytest -v
```

## Resultado Esperado

```text
collected 2 items

tests/test_navegacao.py::test_acessar_pagina_inicial PASSED
tests/test_navegacao.py::test_verificar_titulo_da_pagina PASSED
```

## Análise Crítica

### O cenário escrito ficou compreensível?

Sim. A estrutura Given-When-Then descreve claramente o comportamento esperado do sistema.

### O teste automatizado ficou legível?

Sim. Existe uma relação direta entre os cenários escritos e sua implementação.

### O BDD ajudou a entender o comportamento?

Sim. O foco ficou voltado ao comportamento do usuário e não à implementação técnica.

### Quais dificuldades surgiram?

A identificação de seletores corretos e a configuração inicial do pytest-bdd.

### Os seletores foram frágeis?

Podem se tornar frágeis caso ocorram alterações frequentes na interface.

### O teste ficou dependente da interface?

Sim, pois utiliza elementos visuais da aplicação para validação.

### O cenário representa uma regra de negócio?

Sim. A navegação é uma funcionalidade essencial para utilização do sistema.

### O que tornaria o teste mais robusto?

Utilizar seletores específicos e adicionar validações mais detalhadas sobre os elementos exibidos.

## Reflexão

### BDD melhora a comunicação entre equipe?

Sim. A linguagem utilizada é compreensível para desenvolvedores, QA e stakeholders.

### Todo teste deve ser escrito em BDD?

Não. O BDD é mais indicado para funcionalidades importantes do ponto de vista do negócio.

### Quando vale a pena usar BDD?

Quando existe necessidade de alinhar requisitos, desenvolvimento e qualidade.

### O comportamento ficou mais claro?

Sim. Os cenários descrevem exatamente o que o sistema deve fazer.

### Como isso ajuda no projeto do grupo?

Facilita a comunicação, a documentação viva e a manutenção dos testes ao longo do desenvolvimento.

## Conclusão

A utilização de BDD permitiu documentar comportamentos de forma clara e automatizável. A integração entre pytest-bdd e Playwright possibilitou validar cenários reais do sistema LocalEats mantendo boa legibilidade e organização do projeto.
