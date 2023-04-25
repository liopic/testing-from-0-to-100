Feature: next moon calculation

  Scenario: next moon in December
	Given we set last moon on South to "2022-11-15 19:00:00"
 	 When we ask for the next moon on South from today
 	 Then the next moon on South should be in the future
