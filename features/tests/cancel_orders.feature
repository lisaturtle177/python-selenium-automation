# Created by reneeherscovici at 2/18/22
Feature: User can search for solutions of Canceling an order on Amazon


  Scenario: User uses “Search Help Library” field and searchs for Cancel order
    Given Open Amazon help page
    When  Search for "Cancel order"
    Then  Verify that ‘Cancel Items or Orders’ text is present