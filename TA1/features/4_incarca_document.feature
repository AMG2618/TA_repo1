Feature: Încărcare fișier EMC după autentificare

  Scenario: Utilizatorul se autentifică și încarcă un fișier EMC valid
    Given utilizatorul accesează pagina de login
    When completează câmpul "username" cu "proba12"
    And completează câmpul "password" cu "Alimentare25#"
    And apasă pe butonul "Conectare"
    And navighează către pagina "Incarca fisier"
    And selectează fișierul "Test documente incarcate.pdf"
    And selectează tipul "diploma_emc" din dropdown-ul "tip"
    And selectează valoarea "24" din dropdown-ul "emc"
    And introduce data "08/13/2025" în câmpul "data"
    And apasă pe butonul "Incarca"
    Then ar trebui să apară mesajul de succes "Incarcare reusita"
