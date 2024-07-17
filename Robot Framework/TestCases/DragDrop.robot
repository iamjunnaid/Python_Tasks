# Utilization of the Drag and Drop
*** Settings ***
Library        SeleniumLibrary

*** Test Cases ***
DragDropTEST
    Open Browser    http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html   firefox
    Maximize Browser Window
    Sleep    3
    Drag And Drop    id:box2    id:box102
    Sleep    3
    Drag And Drop    id:box1    id:box101
    Sleep    3
    Drag And Drop    id:box3    id:box103
    Sleep    3
    Drag And Drop    id:box7    id:box107
    Sleep    3
    Drag And Drop    id:box6    id:box106
    Sleep    3
    Drag And Drop    id:box5    id:box105
    Sleep    3
    Drag And Drop    id:box4    id:box104
    Sleep    3
    Close All Browsers
    