Feature: login
 Background:
      Given Navigate to the login page

  @login
  Scenario: Login as standard user with valid credentials
    Given Navigate to the login page
    When Enter "probad1" in the username input field
    And Enter "probad1" in the password input field
    And Click the button "Conectare"
    Then User is redirected to the "https://probaamg.rdsweb.ro/user/\d+$" page
