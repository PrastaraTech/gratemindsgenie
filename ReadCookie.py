import requests


url = 'https://bard.google.com/chat'  # Replace with the URL of the website you want to fetch

# Make a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Accessing the
        # Accessing the cookies from the response
    cookies = response.cookies

    # Print all the cookies set by the website
    print("Cookies:", cookies)

    # If you want to access a specific cookie value by name
    cookie_name = '__Secure-1PSID'
    if cookie_name in cookies:
        cookie_value = cookies[cookie_name]
        print(f"Value of '{cookie_name}' cookie:", cookie_value)
    else:
        print(f"Cookie '{cookie_name}' not found.")
else:
    print("Failed to fetch the website.")

