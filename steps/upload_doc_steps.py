from behave import *
from selenium.webdriver.common.by import By

@given("Navigate to the user page")
def step_impl(context):
    context.upload_doc_page.open()

@when('Click link "Incarca fisier"')
def step_impl(context):
    context.upload_doc_page.click_incarca_fisier_link()

@when('Select file "{filename}"')
def step_impl(context, filename):
    file_path = context.upload_doc_page.get_file_path(filename)
    context.upload_doc_page.choose_file(file_path)

@when('Select "{tip_document}" in the Tip document input field')
def step_impl(context, tip_document):
    context.tip_document = tip_document.strip()   # salvăm tipul documentului
    context.upload_doc_page.select_tip_document(tip_document)

@when('Select "{puncte_emc}" in the Puncte EMC field')
def step_impl(context, puncte_emc):
    if puncte_emc == "<skip>":
        return
    if not hasattr(context, "tip_document") or context.tip_document != "Diploma EMC":
        return
    if not puncte_emc.strip():
        return
    context.upload_doc_page.select_emc(puncte_emc)

@when('Select "{data_emc}" from Data EMC picker')
def step_impl(context, data_emc):
    if context.tip_document != "Diploma EMC":
        return
    if not data_emc.strip():
        return

    context.upload_doc_page.select_date(data_emc)

@when('Click button "Incarca"')
def step_impl(context):
    context.upload_doc_page.click_button_submit()

@then('Message "{text}" displayed')
def step_impl(context, text):
    filename, tip = text.split(" de tipul ")
    assert context.upload_doc_page.verify_document_upload_success(filename, tip), \
        f"Mesajul nu a fost găsit: {text}"
