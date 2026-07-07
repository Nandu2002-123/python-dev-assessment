def filter_and_sort_evens(numbers):
    """
    Takes a list of integers, filters out the odd numbers,
    and returns a new list of even numbers sorted in ascending order.
    """
    return sorted([num for num in numbers if num % 2 == 0])


def count_character_frequency(text):
    """
    Takes a string, converts it to lowercase, and returns a dictionary
    containing the frequency of each character.
    """
    frequency_dict = {}
    for char in text.lower():
        frequency_dict[char] = frequency_dict.get(char, 0) + 1
    return frequency_dict


# ==========================================
# Example Test Cases
# ==========================================

if __name__ == "__main__":
    print("--- Testing Function 1: filter_and_sort_evens ---")
    list_input = [3, 1, 4, 7, 1, 5, 9, 2, 6, 8]
    list_output = filter_and_sort_evens(list_input)
    print(f"Input:  {list_input}")
    print(f"Output: {list_output}\n")

    print("--- Testing Function 2: count_character_frequency ---")
    string_input = "This my task for Basic Data Structures & Algorithms"
    string_output = count_character_frequency(string_input)
    print(f"Input:  '{string_input}'")
    print(f"Output: {string_output}")
