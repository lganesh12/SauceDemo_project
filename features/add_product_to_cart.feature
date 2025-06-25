Feature: Add product to cart

  @TC_03
  Scenario: Add a product to the shopping cart
    Given the user is logged in with username "standard_user" and password "secret_sauce"
    When  the user adds the product "Sauce Labs Backpack" to the cart
    Then  the shopping cart icon should show 1 item
    And   the product "Sauce Labs Backpack" should be listed in the cart
