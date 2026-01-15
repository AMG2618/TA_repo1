from behave import *
from selenium.webdriver.common.by import By


@given("Navigate to the sign-up page")
def step_impl(context):
    #context.browser.driver.get("https://probaamg.rdsweb.ro/inregistrare")
    context.sign_up_page.open()

@when('Enter "{text_user}" in the user input field')
def step_impl(context, text_user):
    context.sign_up_page.fill_user(text_user)
    #context.sign_up_page.set_username(text)

@when('Enter "{text_pass}" in the parola input field')
def step_impl(context, text_pass):
    context.sign_up_page.fill_password(text_pass)

@when('Enter "{text_nume}" in the nume input field')
def step_impl(context, text_nume):
    context.sign_up_page.fill_nume(text_nume)

@when('Enter "{text_prenume}" in the prenume input field')
def step_impl(context, text_prenume):
    context.sign_up_page.fill_prenume(text_prenume)

@when('Enter "{text_colegiu}" in the colegiu input field')
def step_impl(context, text_colegiu):
    context.sign_up_page.fill_colegiu(text_colegiu)

@when('Click the button "Inregistrare"')
def step_impl(context):
    context.sign_up_page.click_inregistrare()

@then('User is redirected to the login "{expected_url}" page')
def step_impl(context, expected_url):
    assert context.sign_up_page.verify_signup_url(expected_url), \
        f"URL did not match: expected pattern: {expected_url}"

@then('Apare un mesaj cu Utilizatorul exista deja in baza de date')
def step_impl(context):
    expected_error = "Eroare! Utilizatorul exista deja in baza de date"
    actual_error = context.sign_up_page.get_error_message()
    assert actual_error == expected_error, f"Expected error message to be '{expected_error}' but got '{actual_error}'"


