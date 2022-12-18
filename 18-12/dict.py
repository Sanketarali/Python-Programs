d={"sanket":9740481350,"Patil":9740481650,"prajwal":9740481520,"Putru":9740481620}
print(d["sanket"])
d["siddu"]=9740481360
print(d)
del d["sanket"]
print(d)

for key in d:
    print(key,d[key])

    if "sanket" in d:
        print("true")
    else:
        print("false")

print(d.clear())