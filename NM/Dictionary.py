def list_operations():
    print("\n--- List Operations ---")

    my_list = list(map(int, input("Enter the elements of the list separated by spaces: ").split()))
    print("Original List:", my_list)

    my_list.append(int(input("Enter a number to append to the list: ")))
    print("After Append:", my_list)

    insert_value = int(input("Enter a number to insert into the list: "))
    insert_index = int(input(f"Enter the index to insert {insert_value} at: "))
    my_list.insert(insert_index, insert_value)
    print("After Insert:", my_list)

    remove_value = int(input("Enter a number to remove from the list: "))
    if remove_value in my_list:
        my_list.remove(remove_value)
        print("After Remove:", my_list)
    else:
        print(f"Value {remove_value} not found in the list.")

    my_list.reverse()
    print("After Reverse:", my_list)

    my_list.sort()
    print("After Sort:", my_list)

    index = int(input("Enter an index to get the element: "))
    if 0 <= index < len(my_list):
        print(f"Element at index {index}:", my_list[index])
    else:
        print("Index out of range.")

def dictionary_operations():
    print("\n--- Dictionary Operations ---")

    n = int(input("Enter the number of key-value pairs for the dictionary: "))
    my_dict = {}
    for _ in range(n):
        key = input("Enter key: ")
        value = input("Enter value: ")
        my_dict[key] = value
    print("Original Dictionary:", my_dict)

    new_key = input("Enter a new key to add: ")
    new_value = input(f"Enter the value for key '{new_key}': ")
    my_dict[new_key] = new_value
    print("After Adding:", my_dict)

    update_key = input("Enter the key to update: ")
    if update_key in my_dict:
        update_value = input(f"Enter the new value for key '{update_key}': ")
        my_dict[update_key] = update_value
        print("After Updating:", my_dict)
    else:
        print(f"Key '{update_key}' not found in the dictionary.")

    remove_key = input("Enter the key to remove: ")
    if remove_key in my_dict:
        my_dict.pop(remove_key)
        print("After Removing:", my_dict)
    else:
        print(f"Key '{remove_key}' not found in the dictionary.")

    query_key = input("Enter a key to get its value: ")
    if query_key in my_dict:
        print(f"Value of '{query_key}':", my_dict[query_key])
    else:
        print(f"Key '{query_key}' not found.")

    print("Keys:", list(my_dict.keys()))
    print("Values:", list(my_dict.values()))

if __name__ == "__main__":
    list_operations()
    dictionary_operations()
