# Gather all the links and Link text from the web URL
# 
*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${URL}           https://wikipedia.com
${BROWSER}       firefox
${LINK_XPATH}    //a
${OUTPUT_FILE}   ${OUTPUT_DIR}/link_texts.txt

*** Test Cases ***
GetAllLinkTest
    [Documentation]    Gather all link texts from the web URL and save them into a file.
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    ${AllLinks}=    Get Element Count    xpath=${LINK_XPATH}
    Log To Console    ${AllLinks}

    @{LinkList}    Create List
    FOR    ${i}    IN RANGE    1    ${AllLinks + 1}
        ${LinkText}=    Get Text    xpath=(${LINK_XPATH})[${i}]
        Log To Console    ${LinkText}
        Append To File    ${OUTPUT_FILE}    ${LinkText}
        Append To File    ${OUTPUT_FILE}    \n
    END
    Close Browser
