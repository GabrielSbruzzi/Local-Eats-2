Feature: Navegação

  Scenario: Acessar página inicial
    Given que o usuário acessa o LocalEats
    When a página carregar completamente
    Then o sistema deve exibir uma página válida

  Scenario: Verificar título da página
    Given que o usuário acessa o LocalEats
    When a página carregar completamente
    Then o título da página deve estar preenchido