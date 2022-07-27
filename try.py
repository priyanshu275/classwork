try:
    1 / 0
except ZeroDivisionError:
    print('Divided by zero')

print('Should reach here')
# -----------------------------------------------------------------------
def divide(x, y):
    try:
        result = x // y
        print("Yeah ! Your answer is :", result)
    except ZeroDivisionError:
        print("Sorry ! You are dividing by zero ")

divide(3, 0)