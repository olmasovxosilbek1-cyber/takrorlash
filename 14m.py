import json

talaba = {
    "ism": "Ali",
    "yosh": 18,
    "ball": 90
}


with open("student.json", "w", encoding="utf-8") as fayl:
    json.dump(talaba, fayl, ensure_ascii=False, indent=4)


with open("student.json", "r", encoding="utf-8") as fayl:
    talaba = json.load(fayl)


print("Ism:", talaba["ism"])
print("Yosh:", talaba["yosh"])
print("Ball:", talaba["ball"])