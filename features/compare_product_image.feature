Feature: Compare product image with baseline

  @TC_04 @not_implemented
  Scenario: Verify product image matches baseline image
    Given the user is logged wants to verify product image matches baseline image
    When  the user navigates to the product details page for "Sauce Labs Backpack"
    Then  the product image should match the baseline image
