Feature: ​ CREATE TAG LIST
In order to : have all useful tags in a list.
As a : admin
I want to : create a list with all tags that spotify provide us from his API.

  Background: There is a registered user
    Given Exists an admin "admin" with password "password"

  Scenario: Create a tag list
    Given I login as admin "admin" with password "password"
    When I create a tag list
      | name        |
      | tag list    |
    Then I'm viewing the tag list by "admin"
      | name        |
      | tag list    |
    And There is 1 tag list