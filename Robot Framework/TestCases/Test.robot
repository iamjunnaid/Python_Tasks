*** Settings ***
Library        SeleniumLibrary

*** Test Cases ***
TEST
    Open Browser    https://google.com    firefox
    Maximize Browser Window
    Sleep     5s
    Close Browser