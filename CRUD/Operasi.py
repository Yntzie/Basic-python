from . import Database
from .Util import randomString
import time
import os

#file ini yang berinteraksi dengan database
def delete(no_buku):
  temp_file_name = "data_temp.txt"
  
  try:
    with open(Database.DB_NAME,'r') as file, \
      open(temp_file_name, 'w', encoding="utf-8") as temp_file:
      counter = 0

      for content in file:
        if counter != no_buku-1:
          temp_file.write(content)
        counter+=1
    os.replace(temp_file_name, Database.DB_NAME)
  except:
    print("database error")

def update(noBuku, pk, data_add, tahun, judul, penulis):
  data = Database.TEMPLATE.copy()
  
  data["pk"] = pk
  data["date_add"] = data_add
  data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
  data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
  data["tahun"] = str(tahun)
  
  data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}'
  
  dataLength = len(data_str)
  
  try:
    with open(Database.DB_NAME,'r+', encoding="utf-8") as file:
      file.seek(dataLength*(noBuku-1))
      file.write(data_str)
  except:
    print("Error update data")

def create(tahun, judul, penulis):
  data = Database.TEMPLATE.copy()
  
  data["pk"] = randomString(6)
  data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
  data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
  data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
  data["tahun"] = str(tahun)
  
  data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'
  
  try:
    with open(Database.DB_NAME, 'a', encoding="utf-8") as file:
      file.write(data_str)
  except:
    print("Gagal create data")
    

def createFirstData():
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
  
  data = Database.TEMPLATE.copy()
  
  data["pk"] = randomString(6)
  data["date_add"] = time.strftime("%Y-%m-%d-%H-%M-%S%z", time.gmtime())
  data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
  data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
  data["tahun"] = str(tahun)
  
  data_str = f'{data["pk"]}, {data["date_add"]}, {data["penulis"]}, {data["judul"]}, {data["tahun"]}\n'
  
  print(data_str)
  try:
    with open(Database.DB_NAME, "w", encoding="utf-8") as file:
      file.write(data_str)
  except:
    print("Gagal membuat")
    
def read(**kwargs):
  try:
    with open(Database.DB_NAME, "r") as file:
      content = file.readlines()
      jumlahBuku = len(content)
      if "index" in kwargs:
        indexBuku = kwargs["index"]-1
        if indexBuku<0 or indexBuku>jumlahBuku:
          return False
        else:
          return content[indexBuku]
      else:
        return content
  except:
    print("Gagal membaca database")
    return False
  