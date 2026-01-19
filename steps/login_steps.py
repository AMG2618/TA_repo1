from behave import *
from behave import then
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@given("Navigate to the login page")
def steps_impl(context):
    context.login_page.open()

@when('Enter "{text}" in the username input field')
def steps_impl(context, text):
    context.login_page.set_username(text)

@when('Enter "{text}" in the password input field')
def steps_impl(context, text):
    context.login_page.set_password(text)

@when('Click the button "Conectare"')
def steps_impl(context):
    context.login_page.click_button_submit()


@then('User is redirected to the "{expected_url}" page')
def step_impl(context, expected_url):
    # expected_url is already a regex string
    assert context.login_page.verify_current_url(expected_url), \
        f"URL did not match: expected pattern: {expected_url}"


