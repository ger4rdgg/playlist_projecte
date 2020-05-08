# Created by m_cho at 08/05/2020
Feature: Create Tag List
  In order to : have all useful tags in a list.
  As a : admin
  I want to : create a list with all tags that spotify provide us from his API.

  Background: There is a registered admin
    Given Exists an admin "admin" with password "password"
    And We have access to Spotify API
    |name     |

  Scenario: Show all tags
    Given I login as admin "admin" and with password "password"
    When I list tags
    Then I'm viewing a list containing
    |name    |
    |tag1    |
    |tag2    |
    |tag3    |
    And The list contains 3 tags