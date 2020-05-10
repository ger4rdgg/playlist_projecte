Feature: List Playlists
  In order to select a playlist,
  As a user
  I want to list all my available playlists.

  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And Exists list registered by user
    |name     |
    |Llista1         |
    |Llista2         |
    |Llista3         |

  Scenario: Show all playlists
    Given I login as user "user" with password "password"
    When I list playlists
    Then I'm viewing a list containing
    |name     |
    |Llista1         |
    |Llista2         |
    |Llista3         |
    And The list contains 3 playlists