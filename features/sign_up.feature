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