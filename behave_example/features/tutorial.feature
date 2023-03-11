Feature: showing off behave

  Scenario Outline: Page responce codes
    Given URL '<url>' as endpoint
    When we open expected page
    Then Verify that code is equal to '<code>'
#    Examples:
#      | url    | code |
#      | first  | 200  |
#      | second | 404  |
#      | third  | 200  |
#      | fourth | 200  |
#      | fifth  | 404  |
#      | six    | 404  |
#      | seven  | 200  |