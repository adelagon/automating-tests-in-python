Feature: users CRUD methods
    As an API user, I should be able to ADD,
    UPDATE, DELETE, and GET users.

    Scenario: Add User
        Given the Users API is sent a random user profile using "POST" method
        Then the response status code is "201"
        And the response contains an "id" field
    
    Scenario: Update User
        Given an existing user, I update its profile with a random "name" using "PUT" method
        Then the response status code is "200"
        And the response "name" field should be equal to the random name

    Scenario: Get User
        Given an existing user, I will get its profile using its "id" and "GET" method
        Then the response status code is "200"
        And the response body should be equal to the latest version of the profile after update

    Scenario: Delete User
        Given an existing user, I will delete it using its "id" and "DELETE" method
        Then the response status code is "200"
        Given the deleted user, I will attempt to get its profile using its "id" and "GET" method
        Then the response status code is "404"
