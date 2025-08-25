Feature: Test the login functionality

  Background: Open the login page
    Given Navigate to the login page

#  @login
#  Scenario: Login as standard user with valid credentials
#    When Enter "proba12" in the username input field
#    And Enter "Alimentare25#" in the password input field
#    And Click the button "Conectare"
#    Then User is redirected to the "https://probaamg.rdsweb.ro/user/\d+$" page

  @signUP
  Scenario: Sign up as a new user
    Given Navigate to the sign-up page
    When Enter "proba1234" in the user input field
    And Enter "Alimentare25#" in the parola input field
    And Enter "IonescuL" in the nume input field
    And Enter "IonA" in the prenume input field
    And Enter "Bucuresti" in the colegiu input field
    And Click the button "Inregistrare"
    Then User is redirected to the login "https://probaamg.rdsweb.ro/login" page