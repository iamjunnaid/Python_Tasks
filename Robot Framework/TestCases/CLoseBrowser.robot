## Simply close the all browsers
*** Settings ***
Library        SeleniumLibrary

*** Test Cases ***
CloseBrowsersTEST
    Open Browser    https://google.com    firefox
    Maximize Browser Window

    Open Browser    https://facebook.com   firefox
    Maximize Browser Window

    Open Browser    https://yahoo.com    firefox
    Maximize Browser Window
    
    Close All Browsers