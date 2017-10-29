*** Settings ***
Library    Selenium2Library

*** Test cases ***
Test
  Open Browser    https://www.google.com    gc
  Sleep    5
  Close All Browsers