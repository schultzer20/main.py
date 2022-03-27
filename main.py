def count_integer(numbers, integer):
    count = 0
    for i in numbers:
        if i == integer:
            count += 1
    if count == 0:
        return 42
    return count


print(count_integer([1, 2, 3, 4, 7, 4, 4], 4))


def list_func(numbers, integer):
    for index, value in enumerate(numbers):
        if value == integer:
            numbers[index] = 6
            print(numbers[::-1])
            return numbers
    else:
        return []


print(list_func([1, 2, 3, 4, 5], 5))


def compare_lists(list1, list2):
    return [i for i in list1 if i in list2]


print(compare_lists([1, 2, 3, 4], [3, 4, 5, 6, 7]))


def remove_duplicates(lst):
    clean_list = []
    for i in lst:
        if i not in clean_list:
            clean_list.append(i)
    return clean_list


print(remove_duplicates([1, 2, 3, 4, 2, 2, 5]))


def dict_func(dictionary):
    dictionary["OS"] = "Linux"
    for key in dictionary:
        print("You have a " + dictionary["Type"] + " from " + dictionary["Brand"] + " that costs: " + dictionary["Price"] + ".")
        print(dictionary)
        break
    return dictionary


my_dict = {"Type": "Notebook", "Brand": "Dell", "Price": "2000"}
print(dict_func(my_dict))
