def shq_pyramid(star):
    i = 0
    while i < star:
        j = 0
        while j < star - i - 1:
            print(' ', end='')
            j += 1
        k = 0
        while k < i + 1:
            print('* ', end='')
            k += 1
        print()
        i += 1

# Call the function with the desired number of rows
shq_pyramid(5)
