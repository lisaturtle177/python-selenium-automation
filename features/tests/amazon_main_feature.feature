# Created by reneeherscovici at 2/26/22
Feature: Tests for Amazon main page

  Scenario: User can see hamburger menu
    Given Open Amazon
    Then Verify hamburger menu present

  Scenario: User can see footer links
    Given Open Amazon
    Then Verify 38 links present

