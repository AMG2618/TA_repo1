Feature: Vizualizare lista documentelor încărcate

  Scenario: Utilizatorul se autentifică și accesează lista documentelor
    Given utilizatorul accesează pagina de login
    When completează câmpul "username" cu "Anita25"
    And completează câmpul "password" cu "Alimentare26#"
    And apasă pe butonul "Conectare"
    And accesează link-ul către lista documentelor încărcate
    Then ar trebui să fie redirecționat către pagina "https://probaamg.rdsweb.ro/fisier/3"
    And mesajul "Lista documentelor incarcate este vizibila" este afișat în consolă
