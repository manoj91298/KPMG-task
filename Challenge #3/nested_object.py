# The function to retrieve values from nested objects and the test cases.

def get_nested_value(obj, key):
    keys = key.split('/')
#       ImageId: ami-02a89066c48741345  # Replace with a suitable AMI for your region
    current = obj   
    for k in keys:
        if k in current:
            current = current[k]
        else:
            return None
    return current

# Test cases
if __name__ == "__main__":
    object1 = {"a": {"b": {"c": "d"}}}
    key1 = "a/b/c"
    print(get_nested_value(object1, key1))  # Output: d

    object2 = {"x": {"y": {"z": "a"}}}
    key2 = "x/y/z"
    print(get_nested_value(object2, key2))  # Output: a

    # Test case for non-existent key
    object3 = {"x": {"y": {"z": "a"}}}
    key3 = "x/y/w"
    print(get_nested_value(object3, key3))  # Output: None

# To execute the script at paticular path:

# "python nested_object.py"

# The script will execute the function get_nested_value with the provided test cases 
