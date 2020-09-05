Feature: Sample - Jsonplaceholder
    This is to test a jsonplaceholder endpoint URL

    @automated
    Scenario: Sample GET Request
        Given I make a GET request to "https://jsonplaceholder.typicode.com/posts"
        Then I expect response status code to be "200"
