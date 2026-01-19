@Regression @Upload

  Feature: Upload documents

  Background:
    Given Navigate to the login page
    When Enter "proba12" in the username input field
    And Enter "Alimentare25" in the password input field
    And Click the button "Conectare"
    Then User is redirected to the "https://probaamg.rdsweb.ro/user/\d+$" page

  @upload-doc
  Scenario Outline: Upload different document type
    When Click link "Incarca fisier"
    And Select file "<file>"
    And Select "<tip_document>" in the Tip document input field
    And Select "<puncte_emc>" in the Puncte EMC field
    And Select "<data_emc>" from Data EMC picker
    And Click button "Incarca"
    Then Message "<file> de tipul <tip_format>" displayed

    Examples:
      | file              | tip_document | tip_format   | puncte_emc | data_emc   |
      | UploadTestDoc.pdf | Diploma EMC  | diploma_emc  | 24 puncte  | 01/15/2026 |
      | image.jpg         | CI           | ci           | <skip      | <skip>     |
