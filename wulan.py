from multiprocessing.sharedctypes import Value


print('nilai tersedia 14,144,54,15,34,574,65,48,54,24')
i = int(input("yang di remove ="))
T = int(input("Masukan nilai yg di tambah = "))
velue = [14,144,54,15,34,574,65,48,54,24,T]
velue.remove(i)

print(velue)


