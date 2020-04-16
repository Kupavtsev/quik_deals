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
    pattern_price = r'\d{5}'    #\w{4}[0-9]
    price_from_string_in_List = re.findall(pattern_price, d[line])
    price_string = str(price_from_string_in_List)
    price_integer = int(price_string[2:-2])
    return price_integer

def time(file_vac, line):
    pattern_time = r'\d\d:\d\d:\d{2}'   #\b\w{2}\b
    time_from_string_in_List = re.findall(pattern_time, d[line])
    pre_time_string = str(time_from_string_in_List)
    time_string = pre_time_string[2:-2]
    return time_string

def size(file_vac, line):
    pattern_size = r'\s\d\s'
    size_list = re.findall(pattern_size, d[line])
    size_string = str(size_list)
    size_integer = int(size_string[4:-4])
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
print('Deal price in first line: ', deal1.price)
deal1.settime(time(d, 1))
print('Time of deal: ', deal1.time)
deal1.setsize(size(d, 1))
print('Deal size: ', deal1.size)
deal1.setside(side(d, 1))
print('Deal side: ', deal1.side)
deal1.settool(tool(d, 1))
print('Deal tool: ', deal1.tool)








#\s\d[0-9][0-9][0-9][0-9] price extract
'''
d_new = {}          
print('__________'*8)

def side(d, line1, line2):              # Проверяем две подряд идущие строки по напровлению сделки
    side_first = d[line1][10:18]        # если разные, первая строка открытие позиции
    print(side_first)                    
    side_second = d[line2][10:18]
    print(side_second)
    print('__________'*8)
    if side_first != side_second:
        return True
    else: pass


if __name__ == '__main__':
    #while True:
        first  = side(d, 1, 2)              
        if first == True:                    
            d_new = d[1]                    # Помещаем в новый словарь строку окрытия позиции. Ключ сохраняется!!!
            d.pop(1)                        # Удаляем из словаря загруженного файла полученую строку полной позиции
            print(d_new)

            # some = d_new.split()
            # print(some)
            # some_dict = {x: for x in some}
            # print(some_dict)
            
            print('__________'*8)
            for key, val in d.items():
                print(key, '=>', val)
        file.close()

'''
#if __name__ == '__main__':