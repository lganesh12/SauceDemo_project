Feature: Compare product image with baseline

  @TC_04
  Scenario: Verify product image matches baseline image
    Given the user is logged in with username "standard_user" and password "secret_sauce"
    When  the user navigates to the product details page for "Sauce Labs Backpack"
    Then  the product image should match the baseline image
