Feature: Sign-up existing user
 Background:
      Given Navigate to the sign-up page

 @sign-up-existing
  Scenario: Sign up with an existing user
    When Enter "proba12" in the user input field
    And Enter "Alimentare25" in the parola input field
    And Enter "Ionescu" in the nume input field
    And Enter "Ion" in the prenume input field
    And Enter "Bucuresti" in the colegiu input field
    And Click the button "Inregistrare"
#    Then Error message "Eroare! Utilizatorul exista deja in baza de date" is displayed
    Then Apare un mesaj cu Utilizatorul exista deja in baza de date