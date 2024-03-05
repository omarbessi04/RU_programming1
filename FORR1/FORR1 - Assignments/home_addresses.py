address = 0
address_list = []
split_adress_list = []

while address != "q":
    address = input()
    if address != "q":
        address_list.append(address)
        
        x, y = address.split()
        split_adress = (x, y)
        split_adress_list.append(split_adress)

print(address_list)
print(split_adress_list)