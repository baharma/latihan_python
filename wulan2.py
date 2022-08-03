

NamaPemilik = input('Nama Pemilik: ')
jumlah = input('Jumlah Sapi: ')
beratSapi = [];
noSapi = [];
jumlahBerat = 0;

for i in range(1, int(jumlah)+1):
    entysapi = input('No Sapi '+str(i)+': ')
    beratsapia = input('Berat Sapi '+str(i)+': ')
    
    beratSapi.append(beratsapia)
    noSapi.append(entysapi)

print("Ternak yang anda miliki:");
print("Nama Ternak :",NamaPemilik);
for i in range(1, int(jumlah)+1):
    print(str(i)+"."+noSapi[i-1]+".berat "+beratSapi[i-1]+"KG");
    jumlahBerat =  int(beratSapi[i-1]) + jumlahBerat;
    
rata = jumlahBerat/int(jumlah)
print("Rata-rata berat ternak anda: "+str(rata));



