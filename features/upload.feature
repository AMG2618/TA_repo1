Feature: Upload documente

#  @login
#  Scenario: Login as standard user with valid credentials
#    Given Navigate to the login page
#    When Enter "proba12" in the username input field
#    And Enter "Alimentare25" in the password input field
#    And Click the button "Conectare"
#    Then User is redirected to the "https://probaamg.rdsweb.ro/user/\d+$" page

  @upload-doc
  Scenario: Upload document
    #Given Navigate to the user page
    Given Navigate to the login page
    When Enter "proba12" in the username input field
    And Enter "Alimentare25" in the password input field
    And Click the button "Conectare"
    Then User is redirected to the "https://probaamg.rdsweb.ro/user/\d+$" page
    When Click link "Incarca fisier"
    And Click button "Choose File"
    And Select file "Test_documente_incarcate.pdf"
    #And Select "Diploma EMC" from dropdown Tip document
    #And Select "24" from dropdown "Puncte EMC"
    #And Select date "08/13/2025" from Data EMC picker
    #And Click button "Incarca"
    #Then Message "A fost incarcat: Test_documente_incarcate.pdf de tipul diploma_emc" displayed
