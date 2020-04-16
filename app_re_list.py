# Version 4
import re
file = open('032.txt', 'r')

# We create dict generator from lines
# and give the number to each line
d = {ix: line for ix, line in enumerate(file)}
# for key, val in d.items():          # Выводит содержимое файла ввиде словаря
#     print(key, '=>', val)
file.close()
print('__________'*8)

def price(file_vac, line):
    pattern_price = r'\d{5}'
    price_from_string_in_List = re.findall(pattern_price, d[line])
    return price_from_string_in_List

def time(file_vac, line):
    pattern_time = r'\d\d:\d\d:\d{2}'
    time_from_string_in_List = re.findall(pattern_time, d[line])
    return time_from_string_in_List

def size(file_vac, line):
    pattern_size = r'\s\d\s'
    size_list = re.findall(pattern_size, d[line])
    size_string = str(size_list)
    size_integer = list(size_string[4:-4])
    return size_integer

def side(file_vac, line):
    try:
        pattern_side = r'\Продажа'
        side_list = re.findall(pattern_side, d[line])
        side_list = 'sold'
        return side_list
    except: pass
    else:
        side_list = 'bought'
        return side_list

def tool(file_vac, line):
    pattern_tool = r'\b\w{4}\b'
    tool_list = re.findall(pattern_tool, d[line])
    return tool_list

class Deal():
    def setprice(self, price):
        self.price = price
    def settime(self, time):
        self.time = time
    def setsize(self, size):
        self.size = size
    def setside(self, side):
        self.side = side
    def settool(self, tool):
        self.tool = tool

deal1 = Deal()
deal1.setprice(price(d, 1))
deal1.settime(time(d, 1))
deal1.setsize(size(d, 1))
deal1.setside(side(d, 1))
deal1.settool(tool(d, 1))

newlist = deal1.price + deal1.time + deal1.size
newlist.append(deal1.side)
newlist = newlist + deal1.tool
print(newlist)

for t in newlist:
    print(type(t), end='')
