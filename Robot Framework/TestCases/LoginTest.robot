*** Settings ***
Library        SeleniumLibrary

*** Test Cases ***
TEST
    Open Browser    https://demo.nopcommerce.com/    firefox
    Click Link    xpath://a[@class='ico-login']