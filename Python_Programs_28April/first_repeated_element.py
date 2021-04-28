def first_repeated_element(str1):
    my_dict = dict()
    str1 = list(str1)
    for i in range(len(str1)):
        if str1[i] not in my_dict:
            my_dict[str1[i]] = 1
        else:
            return str1[i]
    return "No repeated element present"


str1 = input("Enter String: ").strip()
print(first_repeated_element(str1))
