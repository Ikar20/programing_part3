def insertion(array):
    sorted_array = array
    
    for index in range(1, len(sorted_array)):
        element = sorted_array[index];
        j = index - 1
        while j >= 0 and element.duration > sorted_array[j].duration:
            sorted_array[j + 1] = sorted_array[j]
            j -= 1
        sorted_array[j + 1] = element

    return sorted_array
