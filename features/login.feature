Feature: Login

  @TC_01
  Scenario: Successful login
    Given the user is on the SauceDemo login page
    When  the user enters valid login credentials
    And   clicks the login button
    Then  the Products page is displayed

  @TC_02
  Scenario: Unsuccessful login with invalid credentials
    Given the user is on the SauceDemo login page
    When  the user enters invalid login credentials
    And   he clicks the login button
    Then  an error message is displayed
    And   he remains on the login page
