Feature: ​ MODIFY TAGS LIST
In order to : change our tags structure from our tag list.
As a : admin
I want to : add, remove or modify our tags and his moods.

  Background: There is a registered user
    Given Exists an user "user" with password "password"

  Scenario: Modify a tag list
    Given I login as user "user" with password "password"
    When I modify a tag list
      | name        |
      | tag list    |
    Then I'm viewing the tag list by "admin"
      | name        |
      | tag list    |
    And There is 1 tag list