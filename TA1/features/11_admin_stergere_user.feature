Feature: Ștergere utilizator de către administrator

  Scenario: Administratorul se autentifică și șterge un utilizator existent
    Given administratorul accesează pagina de login
    When completează câmpul "username" cu "admin"
    And completează câmpul "password" cu "admin"
    And apasă pe butonul "Conectare"
    And accesează pagina "Lista utilizatori"
    And selectează utilizatorul cu ID-ul 3 pentru ștergere
    Then utilizatorul ar trebui să fie eliminat din listă
