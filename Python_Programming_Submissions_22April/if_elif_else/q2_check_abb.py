def print_subsequent_full_form(str):
    if str == "lol":
        print("Laughing Out Loud")
    elif str == "rolf":
        print("Rolling on the floor laughing")
    elif str == "lmk":
        print("Let Me know")
    else:
        print("Not available") 

str = input("Enter Short Form").strip()
print_subsequent_full_form(str)