## Utilization of the navigational keywords ("Go to" and "Go back")
*** Settings ***
Library        SeleniumLibrary

*** Test Cases ***
NavigationalKeywordTEST
    Open Browser    https://google.com    firefox
    Maximize Browser Window
    ${loca}=    Get Location
    Log To Console    ${loca}
    Sleep    2

    Go To    https://facebook.com
    ${loca}=    Get Location
    Log To Console    ${loca}
    Sleep    2


    Go Back
    ${loca}=    Get Location
    Log To Console    ${loca}
    Sleep    2
    
    Close All Browsers