a = list(map(int, input().split()))
b = sorted(set(a), reverse=True)

if len(b) >=2:
     print("ikkinchi katta son:", b[1])
else:
    print("ikkinchi katta son yoq")

   

