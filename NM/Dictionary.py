def list_operations():
    print("\n--- List Operations ---")

    my_list = [10, 20, 30, 40, 50]
    print("Original List:", my_list)

    my_list.append(60)
    print("After Append (60):", my_list)

    my_list.insert(2, 25)
    print("After Insert (25 at index 2):", my_list)

    my_list.remove(40)
    print("After Remove (40):", my_list)

    my_list.reverse()
    print("After Reverse:", my_list)

    my_list.sort()
    print("After Sort:", my_list)

    print("Element at index 2:", my_list[2])

def dictionary_operations():
    print("\n--- Dictionary Operations ---")
    my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
    print("Original Dictionary:", my_dict)

    my_dict['job'] = 'Engineer'
    print("After Adding ('job': 'Engineer'):", my_dict)

    my_dict['age'] = 26
    print("After Updating ('age': 26):", my_dict)

    my_dict.pop('city')
    print("After Removing ('city'):", my_dict)

    print("Value of 'name':", my_dict['name'])

    print("Keys:", list(my_dict.keys()))

    print("Values:", list(my_dict.values()))

if __name__ == "__main__":
    list_operations()
    dictionary_operations()
