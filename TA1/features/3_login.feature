Feature: Autentificare utilizator existent

  Scenario: Utilizatorul se autentifică cu date valide
    Given utilizatorul accesează pagina de login
    When completează câmpul "username" cu "proba12"
    And completează câmpul "password" cu "Alimentare25#"
    And apasă pe butonul "Conectare"
    Then ar trebui să fie redirecționat către pagina de profil
    And mesajul "Conectare reusita" este afișat în consolă
