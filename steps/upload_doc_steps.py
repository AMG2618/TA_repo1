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
    context.upload_doc_page.select_tip_document(tip_document)

@when('Select "{puncte_emc}" in the Puncte EMC field')
def step_impl(context, puncte_emc):
    if puncte_emc.strip() != "":
        context.upload_doc_page.select_emc(puncte_emc)

@when('Select "{data_emc}" from Data EMC picker')
def step_impl(context, data_emc):
    if data_emc.strip() != "":
        context.upload_doc_page.select_date(data_emc)

@when('Click button "Incarca"')
def step_impl(context):
    context.upload_doc_page.click_button_submit()

@then('Message "{text}" displayed')
def step_impl(context, text):
    filename, tip = text.split(" de tipul ")
    assert context.upload_doc_page.verify_document_upload_success(filename, tip), \
        f"Mesajul nu a fost găsit: {text}"




# ==============================================
# from behave import *
# from features.pages.upload_doc_page import UploadDocumentPage
# from selenium.webdriver.common.by import By
#
#
# @given ("Navigate to the user page")
# def step_impl(context):
#     context.upload_doc_page.open()
#
# @when ('Click link "Incarca fisier"')
# def step_impl(context):
#     context.upload_doc_page.click_incarca_fisier_link()
#
# @when('Click button "Choose File"')
# def step_impl(context):
#     file_path = context.upload_doc_page.get_file_path("UploadTestDoc.pdf")
#     context.upload_doc_page.choose_file(file_path)
#
# # @when('I upload the file from resources')
# # def step_impl(context):
# #     file_path = context.upload_doc_page.get_file_path("UploadTestDoc.pdf")
# #     context.upload_doc_page.choose_file(file_path)
#
#
# # @and ('I upload the file from resources')
# # def step_impl(context):
# #     file_path = context.upload_doc_page.get_file_path("UploadTestDoc.pdf")
# #     context.upload_doc_page.choose_file(file_path)
#
#
# # @when('User selects file "{filename}"')
# # def step_impl(context, filename):
# #     file_path = context.upload_doc_page.get_file_path(filename)
# #     context.upload_doc_page.choose_file(file_path)
#
# # @when ('Select file "Test_documente_incarcate.pdf"')
# # def step_impl(context):
# #     context.upload_doc_page.upload_file_path()
#
# @when ('Select "{text_document}" in the Tip document input field')
# def step_impl(context, text_document):
#     context.upload_doc_page.select_tip_document(text_document)
#
# @when ('Select "{text_emc}" in the Puncte EMC field')
# def step_impl(context, text_emc):
#     context.upload_doc_page.select_emc(text_emc)
#
# @when ('Select "{date_text}" from Data EMC picker')
# def step_impl(context, date_text):
#     context.upload_doc_page.select_date(date_text)
#
# @when ('Click button "Incarca"')
# def step_impl(context):
#     context.upload_doc_page.click_button_submit()
#
# @then('Message "{text_succes}" displayed')
# def step_impl(context, text_succes):
#     assert context.upload_doc_page.verify_document_upload_success(text_succes), "Document upload failed"
