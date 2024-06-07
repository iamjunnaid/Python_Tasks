## Simple Login Setup to the Dummy Website
*** Settings ***
Library        SeleniumLibrary

*** Test Cases ***
LoginTEST
    Open Browser    https://demo.nopcommerce.com/    firefox
    Maximize Browser Window
    Click Link    xpath://a[@class='ico-login']
    Input Text    id:Email        pavanoltraining@gmail.com
    Input Text    id:Password        Test@123
    Click Element    xpath://*[@id="main"]/div/div/div/div[2]/div[1]/div[2]/form/div[3]/button
    Sleep     5s
    Close Browser