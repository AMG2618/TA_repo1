@Regression @Upload

Feature: Upload documents
  Background:
    Given Navigate to the login page

  @upload-doc-emc
  Scenario: Upload document
    When Enter "proba12" in the username input field
    And Enter "Alimentare25" in the password input field
    And Click the button "Conectare"
    Then User is redirected to the "https://probaamg.rdsweb.ro/user/\d+$" page
    When Click link "Incarca fisier"
    And Click button "Choose File"
    And I upload the file from resources
    And Select "Diploma EMC" in the Tip document input field
    And Select "24" in the Puncte EMC field
    And Select "09/21/2025" from Data EMC picker
    And Click button "Incarca"
    Then Message "A fost incarcat: UploadTestDoc.pdf de tipul diploma_emc" displayed

    @upload-doc
    Scenario Outline: Upload different document type
      When Enter "proba12" in the username input field
      And Enter "Alimentare25" in the password input field
      And Click the button "Conectare"
      Then User is redirected to the "https://probaamg.rdsweb.ro/user/\d+$" page
      And Select file "<file>"
      And Select "<tip_document>" in the Tip document input field
      And Select "<puncte_emc>" in the Puncte EMC field
      And Select "<data_emc>" from Data EMC picker
      And Click button "Incarca"
      Then Message "A fost incarcat: Test_documente_incarcate.pdf de tipul diploma_emc" displayed

      Examples:
        | file                         |tip_document      |puncte_emc|data_emc   |
        | UploadTestDoc.pdf            |Diploma EMC      |24        |08/13/2025  |
        | image.jpg                    |CI               |          |            |