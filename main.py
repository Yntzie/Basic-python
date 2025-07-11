import os
import CRUD as CRUD

if __name__ == "__main__":
  sistemOperasi = os.name
  
  match sistemOperasi:
      case "posix" : os.system("clear")
      case "nt" : os.system("cls")
      
  print("Selamat Datang Di Program")
  print("Database Perpustakaan")
  print("=========================")
  
  #check database
  CRUD.initConsole()
  
  while True:
    match sistemOperasi:
      case "posix" : os.system("clear")
      case "nt" : os.system("cls")
      
    print("Selamat Datang Di Program")
    print("Database Perpustakaan")
    print("=========================")
  
    print(f"1. Read Data")
    print(f"2. Create Data")
    print(f"3. Update Data")
    print(f"4. Delete Data\n")
    
    userInput = input("Masukkan opsi anda: ")
    
    match userInput:
      case "1": CRUD.readConsole()
      case "2": CRUD.createConsole()
      case "3": CRUD.updateConsole()
      case "4": CRUD.deleteConsole()
      
    isDone = input("apakah sudah selesai? (y/n) ")
    if(isDone=="y" or isDone=="Y"):
      break
  print("Program selesai")
      