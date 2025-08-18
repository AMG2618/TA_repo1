Feature: Accesare cereri viză EMC de către administrator

  Scenario: Administratorul se autentifică și accesează cererile de viză
    Given administratorul accesează pagina de login
    When completează câmpul "username" cu "admin"
    And completează câmpul "password" cu "admin"
    And apasă pe butonul "Conectare"
    And accesează pagina "Cereri viză EMC"
    Then lista cererilor de viză ar trebui să fie afișată
