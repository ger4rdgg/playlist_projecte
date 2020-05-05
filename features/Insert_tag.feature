Feature: ​ INSERT TAG
In order to : make a successful search of songs.
As a : user
I want to : add tags into the ‘search’ or ‘create’ list bar.

  Background: There is a registered user
    Given Exists an user "user" with password "password"

  Scenario: Insert a tag
    Given I login as user "user" with password "password"
    When I press into a tag
      | name        |
    Then I'm insert the tag by "user"
      | name        |
    And There is 1 tag