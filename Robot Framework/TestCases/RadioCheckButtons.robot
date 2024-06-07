## Simple Radio Buttons and Check Boxes to the Dummy Website
*** Settings ***
Library        SeleniumLibrary

*** Variables ***
${Browser}    firefox
${URL}        https://www.techlistic.com/p/selenium-practice-form.html

*** Test Cases ***
LoginTEST
    Open Browser    ${URL}    ${Browser}
    Maximize Browser Window
    Sleep     5s
    Click Button    xpath://*[@id="ez-accept-all"]
    Sleep    5s
    Select Radio Button    sex    Male
    Select Radio Button    exp    3

    Select Checkbox    Manual Tester

    Sleep    5s
    Close Browser