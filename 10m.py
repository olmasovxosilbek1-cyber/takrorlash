ballar = {
    "Ali": 85,
    "Vali": 92,
    "Sardor": 78,
    "Malika": 95
}
katta= list(ballar.keys())[0]
for ball in ballar:
    if ballar[ball]>ballar[katta]:
        katta=ball

ortacha = sum(ballar.values())/len(ballar)

print(f"eng katta ball: {katta} - {ballar[katta]} ball")
print(f"o'rtacha ball: {ortacha}")