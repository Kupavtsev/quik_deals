file = open('032.txt', 'r')

d = {ix: line for ix, line in enumerate(file)}

def deal(a):
    #print(d[1])
    price = int(d[1][1:7])
    #print(price)
    size = int(d[1][8:9])
    #print(size)
    side_open = d[1][10:18]
    #print(side_open)
    if 'Продажа' in side_open:
        side = 'sold'
    else:
        side = 'bought'
    return price, size, side

open_pos = deal(d)
#print(open_pos)

def deal_next(b):
    #print(d[2])
    price = int(d[2][1:7])
    #print(price)
    size = int(d[2][8:9])
    #print(size)
    side_open = d[2][10:18]
    #print(side_open)
    if 'Продажа' in side_open:
        side = 'sold'
    else:
        side = 'bought'
    return price, size, side

close_pos = deal_next(d)
#print(close_pos)

def calculations(a, b):
    #print(a[1], b[1])
    if a[1] == b[1]:
        if a[2] == 'sold':
            result = ((a[0] - b[0]) * a[1]) - (a[1] * 2)
            #print(result)
    return result

#position1 = calculations(open_pos, close_pos)    