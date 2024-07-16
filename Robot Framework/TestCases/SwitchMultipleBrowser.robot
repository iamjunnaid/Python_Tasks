## Simply simple script to switch between browsers and capture their title
*** Settings ***
Library        SeleniumLibrary

*** Test Cases ***
SwitchBrowsersTEST
    Open Browser    https://google.com    firefox
    Maximize Browser Window
    Sleep    3

    Open Browser    https://facebook.com   firefox
    Maximize Browser Window
    Sleep    3

    Open Browser    https://yahoo.com    firefox
    Maximize Browser Window
    Sleep    3

    Switch Browser    1
    ${title1}=  get title
    Log To Console    ${title1}

    Switch Browser    2
    ${title2}=  get title
    Log To Console    ${title2}

    Switch Browser    3
    ${title3}=  get title
    Log To Console    ${title3}
    
    Close All Browsers