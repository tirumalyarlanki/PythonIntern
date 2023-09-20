def show_numbers(number):
    for i in range(number+1):
        if (i % 2) == 0:
            print(str(i) + " EVEN")
        else:
            print(str(i) + " ODD")
        
number = 3
show_numbers(number)
