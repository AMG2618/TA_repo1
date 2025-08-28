from behave import *

@given ("Navigate to the user page")
def step_impl(context):
    context.upload_doc_page.open()

@when ('Click link "Incarca fisier"')
def step_impl(context):
    context.upload_doc_page.click_incarca_fisier_link()

@when ('Click button "Choose File"')
def step_impl(context):
    context.upload_doc_page.choose_file(r"C:\Users\Localadmin\Downloads\Test documente incarcate.pdf")
    #why previous line return SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 2-3: truncated \UXXXXXXXX escape


@when ('Select file "Test documente incarcate.pdf"')
def step_impl(context):
    context.upload_doc_page.upoad_file_path()

@when ('Select "{text_document}" from dropdown Tip document')
def step_impl(context, tip_document):
    context.upload_doc_page.select_tip_document("text_document")

@when ('Select "{text_emc}" from dropdown Puncte EMC')
def step_impl(context, text_emc):
    context.upload_doc_page.select_emc("text_emc")

@when ('Select "{date_text}" from Data EMC picker')
def step_impl(context, date_text):
    context.upload_doc_page.select_date("date_text")

@when ('Click button "Incarca"')
def step_impl(context):
    context.upload_doc_page.click_button_submit()

@then ('Message "text_succes" displayed')
def step_impl(context):
    assert context.upload_doc_page.verify_document_upload_success(), "Document upload failed"