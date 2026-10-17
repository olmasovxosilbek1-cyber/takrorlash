def tekshir(*son):
    for i in son:
        if i % 2 == 0:
            print(f"{i} juft son")
        else:
            print("Musbat son")
        if  i>0:
            print("Toq son")
  
        else:
            print("Manfiy son")
        return son
son = int(input("sonni kiriting: "))
tekshir(son)
