Feature: Trimitere cerere viză în funcție de punctele EMC

  Scenario Outline: Utilizatorul încearcă să trimită cererea de viză
    Given utilizatorul accesează pagina de login
    When completează câmpul "username" cu "Anita25"
    And completează câmpul "password" cu "Alimentare26#"
    And apasă pe butonul "Conectare"
    And accesează pagina "Documente puncte EMC"
    And verifică că are "48" puncte EMC
    And apasă pe butonul "Cerere viza"
    Then <rezultat>

    Examples:
      | username | password        | puncte_emc     | rezultat                                                                |
      | Anita25  | Alimentare26#   | Total EMC: 0   | mesajul de eroare "Nu aveti suficiente puncte EMC..." este afișat       |
