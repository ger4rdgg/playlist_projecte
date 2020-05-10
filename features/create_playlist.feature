# Created by m_cho at 08/05/2020
Feature: Create Playlist
  In order to : register a playlist.
  As a : user
  I want to : create a list.

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And We have access to Spotify API
      | name |

  Scenario: Register just a list name
    Given I login as user "user" with password "password"
    When I create a tag list
    Then I'm viewing a list containing
      | name |
      | tag1 |
      | tag2 |
      | tag3 |
    And The list contains 3 tags