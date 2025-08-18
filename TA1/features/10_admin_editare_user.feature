Feature: Editare utilizator de către administrator

  Scenario: Administratorul editează datele unui utilizator existent
    Given administratorul accesează pagina de login
    When completează câmpul "username" cu "admin"
    And completează câmpul "password" cu "admin"
    And apasă pe butonul "Conectare"
    And accesează pagina "Lista utilizatori"
    And selectează utilizatorul cu ID-ul 3 pentru editare
    And modifică câmpul "user" cu "Anita25"
    And modifică câmpul "parola" cu "Alimentare26#"
    And modifică câmpul "nume" cu "Anita"
    And modifică câmpul "prenume" cu "Manescu"
    And selectează "Bucuresti" din dropdown-ul "colegiu"
    And apasă pe butonul "Salvează modificările"
    Then ar trebui să fie redirecționat către pagina de profil a utilizatorului
    And mesajul "Modificări efectuate cu succes" este afișat în consolă
