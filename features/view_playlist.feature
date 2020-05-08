Feature: ​ View playlist
  In order to : view spotify playlist.
  As a : user
  I want to : view a customized playlist linked with my tags

  Background: There is a registered user
    Given Exists a user “user” with password “password”
	And Exists a playlist
	|name	|
	|playlist	|

  Scenario: View playlist
    Given I login as a user “user” with password “password”
	When I view a playlist
	Then I see the list of songs in the playlist
	|name|
	|song1	|
	|song2	|
	|song3	|
	And The playlist contains 3 songs