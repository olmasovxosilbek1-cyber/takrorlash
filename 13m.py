try:
    with open("OY3/11-dars/matn.txt", "r") as fayl:
        matn = fayl.read()
    
    sozlar = matn.split()
    print(f"So'zlar soni: {len(sozlar)}")

except FileNotFoundError:
    print("Xatolik: matn.txt fayli topilmadi!")
