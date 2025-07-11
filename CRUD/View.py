from . import Operasi

def deleteConsole():
  readConsole()
  
  while True:
    print("Silahkan pilih nomor buku yang ingin di Delete")
    noBuku = int(input("Nomor Buku: "))
    dataBuku = Operasi.read(index=noBuku)

    if dataBuku:
      data_break = dataBuku.split(',')
      pk = data_break[0]
      data_add = data_break[1]
      penulis = data_break[2]
      judul = data_break[3]
      tahun = data_break[4][:-1]

      #data yang didelete
      print("\n"+"="*100)
      print("Data yang ingin anda hapus")
      print(f"1. Judul\t: {judul:.40}")
      print(f"2. Penulis\t: {penulis:.40}")
      print(f"3. Tahun\t: {tahun:4}")
      
      isDone = input("apakah data yakin di delete? (y/n) ")
      if(isDone=="y" or isDone=="Y"):
        Operasi.delete(noBuku)
        break
    else:
      print("Nomor buku tidak valid silahkan input lagi")
      
  print("Data Berhasil Di hapus")

def updateConsole():
  readConsole()
  while True:
    print("Silahkan pilih nomor buku yang ingin di update")
    noBuku = int(input("Nomor Buku: "))
    dataBuku = Operasi.read(index=noBuku)

    if dataBuku:
      break
    else:
      print("Nomor buku tidak valid silahkan input lagi")
  
    data_break = dataBuku.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]
  
  while True:
    #data yang diupdate
    print("\n"+"="*100)
    print("Silahkan data apa yang ingin anda ubah")
    print(f"1. Judul\t: {judul:.40}")
    print(f"2. Penulis\t: {penulis:.40}")
    print(f"3. Tahun\t: {tahun:4}")
    
    #choose option for update
    userOption = input("Pilih data(1-3): ")
    print("\n"+"="*100)
    match userOption:
      case "1": judul = input("Judul\t: ")
      case "2": penulis = input("Penulis\t: ")
      case "3": 
        while True:
          try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
              break
            else:
              print("Tahun harus angka, silahkan input lagi (yyyy)")
          except:
            print("Tahun harus angka, silahkan input lagi (yyyy)")
      case _: print("index tidak ditemukan")
      
    print("Data Baru Anda")
    print(f"1. Judul\t: {judul:.40}")
    print(f"2. Penulis\t: {penulis:.40}")
    print(f"3. Tahun\t: {tahun:4}")
    
    isDone = input("apakah sudah selesai update? (y/n) ")
    if(isDone=="y" or isDone=="Y"):
      break
  
  Operasi.update(noBuku, pk, data_add, tahun, judul, penulis)
    
def createConsole():
  print("\n"+"="*100)
  print("Silahkan tambah data buku\n")
  penulis = input("Penulis: ")
  judul = input("Judul: ")
  while True:
    try:
      tahun = int(input("Tahun: "))
      if len(str(tahun)) == 4:
        break
      else:
        print("Tahun harus angka, silahkan input lagi (yyyy)")
    except:
      print("Tahun harus angka, silahkan input lagi (yyyy)")
      
  Operasi.create(tahun, judul, penulis)
  print("\nBerikut adalah data baru anda")
  readConsole()

#menampilkan hasil dari operasi
def readConsole():
  dataFile = Operasi.read()
  
  index = "No"
  judul = "Judul"
  penulis = "Penulis"
  tahun = "Tahun"
  
  #ini header
  print("\n"+"="*100)
  print(f"{index:4} | {judul:40} | {penulis:40} | {tahun:5}")
  print("-"*100)
  
  #data
  for index, data in enumerate(dataFile):
    data_break = data.split(",")
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4]
    print(f"{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}", end="")
  
  #ini footer
  print("="*100+"\n")
  