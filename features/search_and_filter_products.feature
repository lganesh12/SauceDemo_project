Feature: Search and filter products on SauceDemo

  @TC_05
  Scenario: Filter products by name ascending (A to Z)
    Given the user is on the SauceDemo login page
    When  the user logs in with username "standard_user" and password "secret_sauce"
    And   the user selects "Name (A to Z)" from the sort dropdown
    Then  the products should be sorted by name in ascending order

  @TC_06
  Scenario: Filter products by name descending (Z to A)
    Given the user is on the SauceDemo login page
    When  the user logs in with username "standard_user" and password "secret_sauce"
    And   the user selects "Name (Z to A)" from the sort dropdown
    Then  the products should be sorted by name in descending order

  @TC_07
  Scenario: Filter products by price low to high
    Given the user is on the SauceDemo login page
    When  the user logs in with username "standard_user" and password "secret_sauce"
    And   the user selects "Price (low to high)" from the sort dropdown
    Then  the products should be sorted by price in ascending order

  @TC_07
  Scenario: Filter products by price high to low
    Given the user is on the SauceDemo login page
    When  the user logs in with username "standard_user" and password "secret_sauce"
    And   the user selects "Price (high to low)" from the sort dropdown
    Then  the products should be sorted by price in descending order
