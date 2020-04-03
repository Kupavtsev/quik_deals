# Version 2

file = open('032.txt', 'r')

# We create dict generator from lines
# and give the number to each line
d = {ix: line for ix, line in enumerate(file)}
#print(len(d))

def deal(d, line):                # From the second line 
    price = int(d[line][1:7])  # we finding price, size and side in the string
    size = int(d[line][8:9])   # and return it
    side_open = d[line][10:18]
    
    if 'Продажа' in side_open:
        side = 'sold'
    else:
        side = 'bought'
    return price, size, side

# We are watching which is Side if the Deal
# and and Sold - Bought = Result
def calculations(a, b):     
    if a[1] == b[1]:        # compare sizes, if sizes the same
        #print('Sides of each deal:', a[2], b[2])
        if a[2] == 'sold':  # compare side is sold
            if a[2] != b[2]:
                rub = ((a[0] - b[0]) * a[1]) - (a[1] * 2)   # a[0] - price, a[1] - size, a[2] - side
                ticks = (a[0] - b[0])
            elif a[2] == b[2]:                              # This is if sizes Equal and sides also Equal
                price = ((a[0] * a[1]) + (b[0] * b[1])) / (a[1] + b[1])
                #print(price)
                size = a[1] + b[1]
                #print(size)
                side = a[2]
                #print(side)
                return price, size, side
                rub = None
                ticks = None
            #else: 
             #   rub = None
              #  ticks = None
    return rub, ticks

if __name__ == '__main__':
# first Deal
    open_one = deal(d, 1)
    close_first =  deal(d, 2)
    position_one = calculations(open_one, close_first)

    print('Rub:', position_one[0], 'ticks:', position_one[1], open_one[2], open_one[1])

# second Deal
    open_two = deal(d, 3)
    #print(55, 'open_two:', open_two)
    close_two =  deal(d, 4)
    #print('close_two:', close_two)
    position_two = calculations(open_two, close_two)
    #print(58, position_two, len(position_two))
    if len(position_two) == 2:  # If situation is straight, First line - Open Position, Second line - Close Position
        #print('position_two:', position_two)
        print('Rub:', position_two[0], 'ticks:', position_two[1], open_two[2], open_two[1])
    elif len(position_two) == 3:
        #print(63, position_two)
        open_two = position_two
        #print(65, open_two)
        close_two = deal(d, 5)
        #print(67, close_two)
        position_two = calculations(open_two, close_two)
        print('Rub:', position_two[0], 'ticks:', position_two[1], open_two[2], open_two[1])

'''
Это тупиковое развитие ситуации.
надо работать с длинной словаря через range.
Т.е. обработать первый словарь строк и создать новый словарь в котором соблюдается поочередность строк:
открытие позиции/закрытие позиции. И удалять эти значения из основного словаря.
И задать ход выполнения в range c ходом через одну строку
'''


