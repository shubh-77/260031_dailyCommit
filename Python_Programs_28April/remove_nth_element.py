def remove_element(str2, i):
    if i < len(str2) and i > 0:
        return str2[:i] + str2[i + 1 :]
    else:
        return "Invalid index"


str1 = input("Enter string").strip()
index = int(input("Enter index to be deleted"))

print(remove_element(str1, index))
