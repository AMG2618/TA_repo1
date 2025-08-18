Feature: Descărcare fișiere din pagina Documente

  Scenario: Utilizatorul se autentifică și descarcă fișierele disponibile
    Given utilizatorul accesează pagina de login
    When completează câmpul "username" cu "proba12"
    And completează câmpul "password" cu "Alimentare25#"
    And apasă pe link-ul către pagina "Documente"
    And setează directorul de descărcare la "C:\Users\Localadmin\Downloads"
    And apasă pe fiecare link "Descarcă fișier"
    Then fișierele ar trebui să fie descărcate cu succes în directorul specificat
