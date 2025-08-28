Feature: Sign-up new user
 Background:
      Given Navigate to the sign-up page

 @sign-up
  Scenario: Sign up as a new user
    When Enter "proba12" in the user input field
    And Enter "Alimentare25" in the parola input field
    And Enter "Ionescu" in the nume input field
    And Enter "Ion" in the prenume input field
    And Enter "Bucuresti" in the colegiu input field
    And Click the button "Inregistrare"
    Then User is redirected to the login "https://probaamg.rdsweb.ro/login" page

 @sign-up-existing
  Scenario: Sign up with an existing user
    When Enter "proba12" in the user input field
    And Enter "Alimentare25" in the parola input field
    And Enter "Ionescu" in the nume input field
    And Enter "Ion" in the prenume input field
    And Enter "Bucuresti" in the colegiu input field
    And Click the button "Inregistrare"
    #Then Error message "Eroare! Utilizatorul exista deja in baza de date" is displayed
    Then Apare un mesaj cu Utilizatorul exista deja in baza de date

  @login
  Scenario: Login as standard user with valid credentials
    Given Navigate to the login page
    When Enter "proba12" in the username input field
    And Enter "Alimentare25" in the password input field
    And Click the button "Conectare"
    Then User is redirected to the "https://probaamg.rdsweb.ro/user/\d+$" page


  @upload-doc
  Scenario: Upload document
    Given Navigate to the user page
    When Click link "Incarca fisier"
    And Click button "Choose File"
    And Select file "Test documente incarcate.pdf"
    And Select "Diploma EMC" from dropdown Tip document
    And Select "24" from dropdown "Puncte EMC"
    And Select date "08/13/2025" from Data EMC picker
    And Click button "Incarca"
    Then Message "A fost incarcat: Test_documente_incarcate.pdf de tipul diploma_emc" displayed


#Feature: Vizualizare lista documentelor încărcate
#  @T5
#  Scenario: Vizualizare documente
#    Given utilizatorul este autentificat
#    When accesează pagina "Documente"
#    Then vede lista fișierelor încărcate
#
#Feature: Descărcare fișiere din pagina Documente
#  @T6
#  Scenario: Descărcare fișier EMC
#    Given utilizatorul este autentificat
#    When accesează pagina "Documente"
#    And apasă pe butonul "Descarcă" pentru fișierul "emc_test.pdf"
#    Then fișierul este descărcat cu succes
#
#Feature: Trimitere cerere viză în funcție de punctele EMC
#  @T7
#  Scenario: Cerere viză cu punctaj suficient
#    Given utilizatorul are peste 200 puncte EMC
#    When accesează pagina "Cerere viză"
#    And completează formularul
#    And apasă pe "Trimite cerere"
#    Then cererea este trimisă cu succes
#
#Feature: Trimitere cerere viză cu punctaj insuficient
#  @T8
#  Scenario: Cerere viză cu punctaj insuficient
#    Given utilizatorul are sub 200 puncte EMC
#    When accesează pagina "Cerere viză"
#    Then apare mesajul "Punctaj insuficient pentru trimiterea cererii"
#
#Feature: Accesare cereri viză EMC de către administrator
#  @T9
#  Scenario: Vizualizare cereri EMC
#    Given administratorul este autentificat
#    When accesează pagina "Cereri EMC"
#    Then vede lista cererilor trimise
#
#Feature: Editare utilizator de către administrator
#  @T10
#  Scenario: Editare date utilizator
#    Given administratorul este autentificat
#    When accesează pagina "Utilizatori"
#    And selectează utilizatorul "medic01"
#    And modifică datele
#    And apasă pe "Salvează"
#    Then apare mesajul "Datele au fost actualizate"
#
#Feature: Ștergere utilizator de către administrator
#  @T11
#  Scenario: Ștergere utilizator
#    Given administratorul este autentificat
#    When accesează pagina "Utilizatori"
#    And selectează utilizatorul "medic01"
#    And apasă pe "Șterge"
#    Then utilizatorul nu mai apare în listă
