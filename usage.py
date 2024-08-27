from base_url import BaseURLSession

# Initialize the session with a base URL
session = BaseURLSession(base_url='https://jsonplaceholder.typicode.com')

print("Base URL:", session.base_url)

# Making a GET request to an endpoint
response = session.get('/posts/1')


# Check the response
if response.status_code == 200:
    print("Request was successful!")
    print("Response Data:", response.json())
else:
    print("Request failed with status code:", response.status_code)
