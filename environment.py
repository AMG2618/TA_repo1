
from browser import Browser
from features.pages.login_page import LoginPage
from features.pages.sign_up_page import SignUpPage
from features.pages.upload_doc_page import UploadDocumentPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.sign_up_page = SignUpPage()
    context.upload_doc_page = UploadDocumentPage()

def after_all(context):
    context.browser.close()

