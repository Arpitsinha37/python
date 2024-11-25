import json

def check_json(json_string, search_key=None, search_value=None):
    """
    Checks if a JSON string contains a specific key or value.

    :param json_string: The JSON string to parse and search.
    :param search_key: The key to search for (optional).
    :param search_value: The value to search for (optional).
    :return: A dictionary with the results.
    """
    try:
        # Parse the JSON string
        data = json.loads(json_string)
        
        # Initialize results
        results = {
            "key_found": False,
            "value_found": False
        }

        # Search for the key if provided
        if search_key is not None:
            results["key_found"] = search_key in data if isinstance(data, dict) else False
        
        # Search for the value if provided
        if search_value is not None:
            def contains_value(d, value):
                if isinstance(d, dict):
                    return value in d.values() or any(contains_value(v, value) for v in d.values())
                elif isinstance(d, list):
                    return any(contains_value(i, value) for i in d)
                else:
                    return d == value

            results["value_found"] = contains_value(data, search_value)
        
        return results
    
    except json.JSONDecodeError:
        return "Invalid JSON string"


# Example usage
json_string = '{"name": "John", "age": 30, "city": "New York"}'

# Check for key
print(check_json(json_string, search_key="name"))  # {'key_found': True, 'value_found': False}

# Check for value
print(check_json(json_string, search_value="New York"))  # {'key_found': False, 'value_found': True}

# Check for both
print(check_json(json_string, search_key="age", search_value=30))  # {'key_found': True, 'value_found': True}

# Invalid JSON
print(check_json("Invalid JSON", search_key="name"))  # Invalid JSON string
