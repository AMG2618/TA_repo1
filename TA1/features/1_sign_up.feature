
@Login @Smoke
Feature: Înregistrare utilizator nou pe platforma Medici

  Scenario: Utilizatorul se înregistrează cu date valide
    Given utilizatorul accesează pagina de înregistrare
    When completează câmpul "user" cu "proba12"
    And completează câmpul "parola" cu "Alimentare25#"
    And completează câmpul "nume" cu "Anita"
    And completează câmpul "prenume" cu "Popiescu"
    And selectează "Brasov" din dropdown-ul "colegiu"
    And apasă pe butonul "Inregistrare"
    Then ar trebui să fie redirecționat către pagina de login
    And mesajul "Inregistrare reusita" este afișat în consolă

