def replace_repeated(c):
    my_dict = dict()
    c = list(c)
    for i in range(len(c)):
        if c[i] not in my_dict.keys():
            my_dict[c[i]] = 1
        else:
            c[i] = "$"
    return "".join(c)


str1 = input("Enter string")
print(replace_repeated(str1))
