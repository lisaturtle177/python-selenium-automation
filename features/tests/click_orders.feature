# Created by reneeherscovici at 2/18/22
Feature: Logged out user sees Sign in page when clicking Orders


  Scenario: User clicks orders when not logged in, sees sign in page
    Given Open Amazon homepage
    When  Click Orders
    Then Verify user is brought to signin page