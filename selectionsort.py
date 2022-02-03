def index_of_min(list_of_elements, start_index):
    min_index = start_index
    min_value = list_of_elements[min_index]

    print("starting from elem: " + str(min_value))
    for i in range(min_index, len(list_of_elements)):
        print("comparison b/w: " + str(list_of_elements[i]) + " and " + str(min_value))
        if list_of_elements[i] < min_value:
            min_value = list_of_elements[i]
            min_index = i
            print("the small elem is now " + str(min_value))
        else:
            pass
    
    return min_index

def swap(list_of_elements, first_index, second_index):
    temp = list_of_elements[first_index]
    list_of_elements[first_index] = list_of_elements[second_index]
    list_of_elements[second_index] = temp
    return list_of_elements

def selection_sort(list_of_elems):
    sorted_list = list_of_elems
    for i in range(len(list_of_elems)):
        index = index_of_min(sorted_list, i)
        print("min index: " + str(index))
        sorted_list = swap(sorted_list, i, index)
    
    return sorted_list
    


nums = [20, 25, 4, 6, 10, 40]

my_list = selection_sort(nums)
print(my_list)