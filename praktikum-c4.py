#Praktikum 4
nim = ['2','3','1','0','3','1','0','6','9']

print(nim)

print('item indeks 0 (pertama)',nim[0])
print('item indeks 1 (kedua)',nim[1]) 

print(f'item indeks 0 (pertama) {nim[0]}')
print(f'item indeks 1 (kedua) {nim[1]}')
print(f'item indeks terakhir {nim[len(nim)-1]}')
print(f'item indeks terakhir {nim[-1]}')
print(f'iten indeks (pertama) {nim[-len(nim)]}')
print()

#LATIHAN LIST
data = ['Sarvina Sari',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama:'+ data[0])
print('angkatan:', data[1])
print('status:'+ data[2])
print()
print(f'{data[0]} status kuliah: {data[2]}')
print(f'Data terbesar nilai adalah: {max(nilai)}')
print(f'Data terbesar nilai adalah: {min(nilai)}')
print(f'Rata-rata nilai adalah: {sum(nilai)/len(nilai)}')
print()        
