Feature: SauceDemo Login Functionality

  @TC_01
  Scenario Outline: Verify login with various credentials combinations
    Given the user is on the SauceDemo login page
    When  the user enters <username> and <password>
    And   he clicks the login button
    Then  the user should <expected_result>

    Examples:
      | username        | password       | expected_result                |
      | standard_user   | secret_sauce   | the Products page is displayed |
      | invalid_user    | wrong_password | an error message is displayed  |
      | locked_out_user | secret_sauce   | the locked out error appears   |
