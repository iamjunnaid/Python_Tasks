# How to Take the screen shot of an element and page
*** Settings ***
Library        SeleniumLibrary

*** Test Cases ***
NavigationalKeywordTEST
    Open Browser    https://wikipedia.org    firefox
    Maximize Browser Window
    Capture Element Screenshot    xpath://*[@id="www-wikipedia-org"]/main/div[1]/h1/span   logo.png
    Capture Page Screenshot    LogoPage.png