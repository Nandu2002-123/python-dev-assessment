import requests


def fetch_and_display_users(num_users):
    """
    Fetches user data from JSONPlaceholder API and displays name, email, and city.
    Handles network errors, bad status codes, and missing dictionary keys.
    """
    url = "https://jsonplaceholder.typicode.com/users"

    try:
        # 1. Make the GET request
        response = requests.get(url, timeout=10)

        # 2. Check for HTTP status code errors (e.g., 404, 500)
        response.raise_for_error() if hasattr(response, 'raise_for_error') else None
        if response.status_code != 200:
            print(f"Error: Server returned unexpected status code {response.status_code}")
            return None

        # 3. Parse JSON response
        users = response.json()

        if not isinstance(users, list):
            print("Error: Expected a list of users, but received a different JSON format.")
            return None

        print(f"\n--- Displaying up to {num_users} users (Available: {len(users)}) ---")

        # 4. Iterate and print with safe key extraction
        for i, user in enumerate(users[:num_users]):
            try:
                name = user["name"]
                email = user["email"]
                city = user["address"]["city"]
                print(f"User {i + 1}: {name} | Email: {email} | City: {city}")
            except KeyError as ke:
                print(f"Error: Missing expected key {ke} in user data at index {i}.")
                continue  # Skip to the next user if one is corrupted

    except requests.exceptions.Timeout:
        print("Error: The request timed out. Please check your internet connection.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: Failed to connect to the server. Network is down.")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Network Error occurred: {e}")
        return None
    except ValueError:
        print("Error: Failed to parse response as JSON.")
        return None


# ==========================================
# TEST CASES
# ==========================================
if __name__ == "__main__":
    # Test case 1: Fetch 4 users
    fetch_and_display_users(4)

    # Test case 2: Fetch 16 users (API maxes out at 10)
    fetch_and_display_users(16)




