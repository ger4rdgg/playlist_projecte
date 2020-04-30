Feature: ​ REMOVE TAG
In order to : make a more accurate search of songs.
As a : user
I want to : remove tags from the ‘search’ or ‘create’ list bar.

  Background: There is a registered user
    Given Exists an user "user" with password "password"

  Scenario: Remove a tag
    Given I login as user "user" with password "password"
    When I press into a tag
      | name        |
    Then I remove the tag by "user"
      | name        |
    And There is 1 tag