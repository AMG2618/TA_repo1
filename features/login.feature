Feature: Test the login functionality

  Background: Open the login page
    Given Navigate to the login page

  @login
  Scenario: Login as standard user with valid credentials
    When Enter "proba12" in the username input field
    And Enter "Alimentare25#" in the password input field
    And Click the button "Conectare"
    Then User is redirected to the "https://probaamg.rdsweb.ro/user/\d+$" page