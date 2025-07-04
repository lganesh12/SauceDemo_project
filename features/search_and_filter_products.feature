Feature: Search and filter products on SauceDemo

  @TC_05 @not_implemented
  Scenario: Filter products by name ascending (A to Z)
    Given the user wants to filter products by name ascending
    When  the user logs in with username "standard_user" and password "secret_sauce"
    And   the user selects "Name (A to Z)" from the sort dropdown
    Then  the products should be sorted by name in ascending order

  @TC_06 @not_implemented
  Scenario: Filter products by name descending (Z to A)
    Given tthe user wants to filter products by name descending
    When  the user logs in with username "standard_user" and password "secret_sauce"
    And   the user selects "Name (Z to A)" from the sort dropdown
    Then  the products should be sorted by name in descending order

  @TC_07 @not_implemented
  Scenario: Filter products by price low to high
    Given the user wants to filter products by price low to high
    When  the user logs in with username "standard_user" and password "secret_sauce"
    And   the user selects "Price (low to high)" from the sort dropdown
    Then  the products should be sorted by price in ascending order

  @TC_07 @not_implemented
  Scenario: Filter products by price high to low
    Given the user wants filter products by price high to low
    When  the user logs in with username "standard_user" and password "secret_sauce"
    And   the user selects "Price (high to low)" from the sort dropdown
    Then  the products should be sorted by price in descending order
