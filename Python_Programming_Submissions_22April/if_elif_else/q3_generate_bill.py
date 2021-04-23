def generate_pizza_bill(slices):
   #prints bill
    print("You will pay ${}".format(120.00 * slices if slices %2 == 0 else 123.00 * slices))

slice = input()
slice = int(slice)
generate_pizza_bill(slice)