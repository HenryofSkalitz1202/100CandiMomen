def my_split(string, delimiter):  # Pengganti fungsi split()
    len_substrings = 1
    for i in range(len(string)):
        if string[i] == delimiter:
            len_substrings += 1

    substrings = ['' for x in range(len_substrings)]
    current_substring = ''
    idx = 0
    for i in range(len(string)-1):
        if string[i] == delimiter:
            substrings[idx] = current_substring
            current_substring = ''
            idx += 1
        elif string[i]+string[i+1] != '\n':
            current_substring += string[i]
    substrings[len_substrings-1] = current_substring
    return substrings


def remove_sesuatu(string, elem):
    hasil = ''
    for i in range(len(string)):
        if string[i] != elem:
            hasil += string[i]
    return hasil


def sort_array_candi(arr):
    for i in range(99):
        for j in range(0, 99-i):
            if arr[j][1] == larger_string(arr[j][1], arr[j+1][1]):
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


def larger_string(str1, str2):
    if len(str1) <= len(str2):
        smaller_len = len(str1)
        largerstring = str2
    else:
        smaller_len = len(str2)
        largerstring = str1

    for i in range(smaller_len):
        if str1[i].upper() > str2[i].upper():
            largerstring = str1
            break
        elif str2[i].upper() > str1[i].upper():
            largerstring = str2
            break
    return largerstring


def linearCongruentialMethod(Xo, m, a, c, randomNums, noOfRandomNums):
    # Initialize the seed state
    randomNums[0] = Xo
    # Traverse to generate required numbers of random numbers
    for i in range(1, noOfRandomNums):
        # Follow the linear congruential method
        randomNums[i] = ((randomNums[i - 1] * a) + c) % m
