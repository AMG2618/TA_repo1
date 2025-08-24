

from features.pages.login_page import LoginPage
from browser import Browser
from features.pages.sign_up_page import SignUpPage


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.sign_up_page = SignUpPage()

def after_all(context):
    context.browser.close()

