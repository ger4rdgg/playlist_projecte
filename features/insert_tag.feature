Feature: Insert Tag
In order to : make a successful search of songs.
As a : user
I want to : add tags into the ‘search’ or ‘create’ list bar.

   Background: There is a registered user
    Given Exists a user "user" with password "password"
    And Exists list registered by user
    |name     |
    |Llista1         |
    |Llista2         |
    |Llista3         |

  Scenario: Show all tags
    Given I login as user "user" and with password "password"
    When I press a tag
    Then Insert a tag into the tag bar
    |name     |
    |tag1           |
    And The list contains 1 tag