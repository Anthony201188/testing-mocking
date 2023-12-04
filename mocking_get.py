""" Exercise(Mocking a GET Request in Python):
You are tasked with writing a Python function that performs a GET request using the requests library. Your function, get_data(url),
takes a URL as an argument and returns the JSON response if the status code is 200. If the status code is not 200, the function should return None.

Your task is to write unit tests for the get_data function, specifically focusing on mocking the GET request using the unittest.mock module. 
You should simulate both a successful request (status code 200) and a failed request (status code other than 200) to test the behavior of the 
function under different scenarios.

Instructions:
Implement the get_data(url) function according to the given specifications. Use the requests library to make the GET request and handle the response appropriately.
Write unit tests for the get_data function using the unittest module.
Use the @patch decorator from unittest.mock to mock the requests.get method in your tests.
Write a test method, test_get_data_success, to simulate a successful GET request. Configure the mock response to have a status code of 200 and a JSON body with a 'message' key set to 'Success'. Verify that the function returns the expected JSON response.
Write a test method, test_get_data_failure, to simulate a failed GET request. Configure the mock response to have a status code other than 200 (e.g., 404) and a JSON body with a 'message' key set to 'Not Found'. Verify that the function returns None in this case.
Run the tests (with unittest or pytest)

Note:
Ensure that you import the necessary modules and libraries (requests, unittest, unittest.mock) in your code.
The requests.get method should not be actually called during the execution of the tests. It should be mocked to simulate the behavior of a real GET request. """

import requests

url = "https://translate.google.com/history" #<- Testing URL returns Json with time a date

def get_data(url):
    response = requests.get(url)
    #data = response.json()
    #status = response.status_code

    if response.status_code == 200:
        return response.text
    
    else:
        print(f"An error has occured, status code {response.status_code}")
        return None

returned_data = get_data(url)
print(type(returned_data))
results = 0

if "button" in returned_data:
    results += 1

print(results)
    


