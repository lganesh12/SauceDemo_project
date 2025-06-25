Feature: Validate cart details

  @TC_08
  Scenario: Verify cart details after adding a product
    Given the user is logged in with username "standard_user" and password "secret_sauce"
    And   the user has added the product "Sauce Labs Backpack" to the cart
    When  the user navigates to the shopping cart page
    Then  the cart should contain 1 item
    And   the product name should be "Sauce Labs Backpack"
    And   the product price should be "$29.99"
