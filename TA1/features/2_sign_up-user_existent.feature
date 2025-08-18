Feature: Înregistrare eșuată cu utilizator existent

  Scenario: Utilizatorul încearcă să se înregistreze cu un username deja existent
    Given utilizatorul accesează pagina de înregistrare
    When completează câmpul "user" cu "proba12"
    And completează câmpul "parola" cu "Alimentare25#"
    And completează câmpul "nume" cu "Anita"
    And completează câmpul "prenume" cu "Popiescu"
    And selectează "Brasov" din dropdown-ul "colegiu"
    And apasă pe butonul "Inregistrare"
    Then ar trebui să apară mesajul de eroare "Eroare! Utilizatorul exista deja in baza de date"
    And mesajul este afișat în consolă
