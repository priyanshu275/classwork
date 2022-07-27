


try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
# ------------------------------------------------------
    a = ["Python", "Exceptions", "try and except"]
    try:
        for i in range(4):
            print("The index and element from the array is", i, a[i])
    except:
        print("Index out of range")

#-----------------------------------------------------------

def square_root(Number):
    assert (Number < 0), "Give a positive integer"
    return Number ** (1 / 2)


# Calling function and passing the values
print(square_root(36))
print(square_root(-36))


num = [3, 4, 5, 7]
if len(num) > 3:
    raise Exception( f"Length of the given list must be less than or equal to 3 but is {len(num)}" )


