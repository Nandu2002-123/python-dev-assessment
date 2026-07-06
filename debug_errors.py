def calculate_average(numbers):
    """
    Calculates the average of a list of numbers.
    Gracefully handles empty lists by returning None.
    """
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]

    try:
        return total / len(numbers)
    except ZeroDivisionError:
        # Documented choice: Returning None for an empty list
        return None


def get_list_element(my_list, index):
    """
    Retrieves an element from a list at a specified index.
    Handles IndexError and TypeError gracefully.
    """
    try:
        return my_list[index]
    except IndexError:
        print(f"Error: Index {index} is out of bounds for the list.")
        return None
    except TypeError:
        print(f"Error: Expected a list-like object, but received type '{type(my_list).__name__}'.")
        return None


# ==========================================
# TEST CASES
# ==========================================
if __name__ == "__main__":
    # --- Part 1: Average Calculation Testing ---
    print("--- Testing calculate_average ---")
    data1 = [10, 20, 30, 40, 50]
    data2 = [5, 15]
    data3 = []  # Triggers the ZeroDivisionError catch

    print(f"Average of data1: {calculate_average(data1)}")  # Output: 30.0
    print(f"Average of data2: {calculate_average(data2)}")  # Output: 10.0
    print(f"Average of data3: {calculate_average(data3)}")  # Output: None
    print()

    # --- Part 2: Element Retrieval Testing ---
    print("--- Testing get_list_element ---")
    sample_list = ["apple", "banana", "cherry"]

    # Valid Input
    print("Valid Call:", get_list_element(sample_list, 1))

    # Out-of-bounds Input (Triggers IndexError)
    print("Out of Bounds:", get_list_element(sample_list, 10))

    # Incorrect Type Input (Triggers TypeError)
    print("Incorrect Type:", get_list_element(42, 0))
