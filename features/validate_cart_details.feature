Feature: Validate cart details

  @TC_08 @not_implemented
  Scenario: Verify cart details after adding a product
    Given the user wants to Verify cart details after adding a product
    And   the user has added the product "Sauce Labs Backpack" to the cart
    When  the user navigates to the shopping cart page
    Then  the cart should contain 1 item
    And   the product name should be "Sauce Labs Backpack"
    And   the product price should be "$29.99"
