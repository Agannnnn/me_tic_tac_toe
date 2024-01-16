import os

papan = [
  ["_","_","_"],
  ["_","_","_"],
  ["_","_","_"],
]

def liat_papan():
  for y in range(3):
    print(f"{papan[y][0]} {papan[y][1]} {papan[y][2]}")

def update_papan(x=int, y=int, val=str):
  if papan[y][x] != "_":
    return -1
  
  papan[y][x] = val
  if cek_horizontal(x,y) or cek_vertikal(x,y) or cek_diagonal(x,y):
    return 1

  return 0

def cek_horizontal(x=int, y=int):
  baris = [val for val in papan[y] if val == papan[y][x]]
  if len(baris) == 3:
    return True
  return False

def cek_vertikal(x=int, y=int):
  baris = [val for val in [papan[i][x] for i in range(3)] if val == papan[y][x]]
  if len(baris) == 3:
    return True
  return False

def cek_diagonal(x=int, y=int):
   baris_kiri = [papan[i][i] for i in range(3) if papan[i][i] == papan[y][x]]
   baris_kanan = [papan[i][j] for i in range(3) for j in range(2, 0, -1) if papan[i][i] == papan[y][x]]
   if len(baris_kanan) == 3 or len(baris_kiri) == 3:
     return True
   return False


giliran = 0

while True:
  os.system("cls")
  
  liat_papan()
  val = "x" if giliran == 0 else "y"

  print(f"Sekarang giliran {"x" if giliran == 0 else "y"}")
  
  print("Masukkan koordinat (0,0 -> 2,2):")
  koordinat = input("(format: x y) ")

  (x, y) = koordinat.split(" ")

  res = update_papan(int(x), int(y), val)

  if res == 0:
    giliran = 1 if giliran == 0 else 0
    val = "x" if giliran == 0 else "y"
  if res == 1:
    os.system("cls")
  
    print("Game Selesai!")

    liat_papan()
    print("Luh menang banh 🙏")
    break