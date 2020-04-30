Feature: ​ VIEW TAGS LIST
In order to : be informed of the tags that we can use.
As a : user
I want to : see on our screen all the tags from the tags list.

  Background: There is a registered user
    Given Exists an user "user" with password "password"

  Scenario: View tag list
    Given I login as user "user" with password "password"
    When I press into  view taglist.
      | name        |
      | tag list    |
    Then I'm viewing the tag list by "admin"
      | name        |
      | tag list    |
    And There is 1 tag list