Feature: ​ CREATE AND VIEW PLAYLIST
In order to : have a customized spotify playlist.
As a : user
I want to : create a custom playlist linked with our moods and tags once we press the create
button, and be able to see it once the creation has finished.

  Background: There is a registered user
    Given Exists user "user" with password "password"

  Scenario: Create a playlist
    Given I login as user "user" with password "password"
    When I create a playlist
      | name        |
      | playlist    |
    Then I'm viewing the playlist by "user"
      | name        |
      | playlist    |
    And There is 1 playlist