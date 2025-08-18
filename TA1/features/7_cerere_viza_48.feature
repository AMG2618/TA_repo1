Feature: Trimitere cerere viză în funcție de punctele EMC

  Scenario: Utilizatorul trimite cererea de viză cu exact 48 puncte EMC
    Given utilizatorul accesează pagina de login
    When completează câmpul "username" cu "Anita25"
    And completează câmpul "password" cu "Alimentare26#"
    And apasă pe butonul "Conectare"
    And accesează pagina "Documente puncte EMC"
    And verifică că are "Total EMC: 48"
    And apasă pe butonul "Cerere viza"
    Then cererea de viză ar trebui să fie trimisă cu succes
    And afiseaza mesaj de confirmare "A fost trimisa cu succes cererea de viză."

