# Created by m_cho at 08/05/2020
Feature: ​ MODIFY TAG LIST
  In order to : change our tags structure from our tag list.
  As a : admin
  I want to : add, remove or modify our tags and his moods.

  Background: There is a registered admin
    Given Exists an admin "admin" with password "password"
    And There is a tag list created

    |name     |
    |tag list |

  Scenario: Modify tag list
    Given I login as admin "admin" and with passwowrd "password"
    When I modify a tag
    Then I'm viewing the tag list modified
    |name    |
    |tag list    |
    And The list is modified