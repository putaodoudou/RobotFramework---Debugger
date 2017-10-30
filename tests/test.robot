*** Settings ***
Library    Selenium2Library

*** Test Cases ***
Test
  [Documentation]
  ...    Test Docs
  [Setup]    Open Browser    https://www.google.com    gc
  Log    Start Test
  Keyword Thing
  Log    End Test
  [Teardown]    Close All Browsers

*** Keywords ***
Keyword Thing
  [Documentation]
  ...   Keyword Docs
  Log    Start Keyword Thing
  Sleep    5
  Log    End Keyword Thing