from linked_list import LinkedList

if __name__ == "__main__":
    """
    Use this file to create a LinkedList instance and perform operations
    like insertion, recursion-based sum, search, and reverse.
    """

    # 1) Create a LinkedList instance
    employee_ids = LinkedList()

    # 2) Insert some sample data using insert_at_front
    employee_ids.insert_at_front(105)
    employee_ids.insert_at_front(210)
    employee_ids.insert_at_front(315)
    employee_ids.insert_at_front(420)
    employee_ids.insert_at_front(525)

    # 3) Display the list to verify insertion
    print("Original Employee ID List:")
    employee_ids.display()

    # 4) Call recursive_sum and print the result
    total = employee_ids.recursive_sum()
    print("\nSum of Employee IDs:", total)

    # 5) Call recursive_search with a target and print result
    target = 315
    if employee_ids.recursive_search(target):
        print(f"Employee ID {target} was found.")
    else:
        print(f"Employee ID {target} was not found.")

    # 6) Call recursive_reverse, then display the reversed list
    employee_ids.recursive_reverse()
    print("\nReversed Employee ID List:")
    employee_ids.display()