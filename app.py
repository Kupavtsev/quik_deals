# Version 1

file = open('032.txt', 'r')

# We create dict generator from lines
# and give the number to each line
d = {ix: line for ix, line in enumerate(file)}
#print(len(d))

def deal(x):                # From the second line 
    price = int(d[1][1:7])  # we finding price, size and side in the string
    size = int(d[1][8:9])   # and return it
    side_open = d[1][10:18]
    
    if 'Продажа' in side_open:
        side = 'sold'
    else:
        side = 'bought'
    return price, size, side

def deal_next(x):           # This is next line in file
    price = int(d[2][1:7])  # The same as def(deal)
    size = int(d[2][8:9])   # It used for 'closing' position
    side_open = d[2][10:18]
    
    if 'Продажа' in side_open:
        side = 'sold'
    else:
        side = 'bought'
    return price, size, side

# We are watching which is Side if the Deal
# and and Sold - Bought = Result
def calculations(a, b):     
    if a[1] == b[1]:        # compare sizes
        if a[2] == 'sold':  # compare side
            rub = ((a[0] - b[0]) * a[1]) - (a[1] * 2)
            ticks = (a[0] - b[0])
    return rub, ticks

#First Deal
open_first = deal(d)
close_pos = deal_next(d)
position_one = calculations(open_first, close_pos)

print('Rub:', position_one[0], 'ticks:', position_one[1], open_first[2], open_first[1])

#Second Deal
