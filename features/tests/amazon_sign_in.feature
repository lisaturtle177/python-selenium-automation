# Created by reneeherscovici at 3/7/22
Feature: Amazon sign in tests

  Scenario: Sign in page can be opened from Sign in popup
    Given Open Amazon
    When Click on button from Sign in popup
    Then Verify Sign in page is opened
