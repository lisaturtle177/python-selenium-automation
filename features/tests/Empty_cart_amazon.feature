# Created by reneeherscovici at 2/23/22
Feature: User can click cart and verify it is empty
  # Enter feature description here

  Scenario: User clicks on the cart icon and verifies Amazon Cart is empty
    Given Open Amazon home page
    When Clicks on the cart icon
    Then Verify that Your Amazon Cart is empty


