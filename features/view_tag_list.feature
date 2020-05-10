Feature: View Tags List
In order to : be informed of the tags that we can use.
As a : user
I want to : see on our screen all the tags from the tags list.

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    |name     |
    |tag1           |
    |tag2           |
    |tag3           |

  Scenario: Show all tags
    Given I login as user "user" with password "password"
    When I list tags
    Then I'm viewing a list of tags
    |name     |
    |tag1          |
    |tag2          |
    |tag3          |
    And The list contains 3 tags