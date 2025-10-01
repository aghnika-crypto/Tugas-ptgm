# statement elif
nilai = int(input("Masukkan nilai kamu: "))
if nilai >= 100:
    print("Nilai kamu: A")
elif nilai >= 80:
    print("Nilai kamu: B")
elif nilai >= 75:
    print("Nilai kamu: C")
elif nilai >= 50:
    print("Nilai kamu: D")
else:
    print("Nilai kamu: E (Kamu tidak lulus)")