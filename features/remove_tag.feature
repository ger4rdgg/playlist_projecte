# Created by m_cho at 08/05/2020
Feature: ​ Remove tag
  In order to : make a more accurate search of songs.
  As a : user
  I want to : remove tags from the ‘search’ or ‘create’ list bar.
  Background: There is a registered user
    Given Exists a user "user" with password "password"
    And There is a tag in the search bar
    |name     |
    |tag      |

  Scenario: Delete tag
    Given I login as user "user" with password "password"
    When I delete a tag
    Then I'm not viewing the tag in the search bar
    |name    |

    And The tag is removed