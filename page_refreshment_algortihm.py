
arr = {}
ints = [2,3,2,1,5,2,4,5,3,2,5,2]
hit = 0
miss = 0
i = 0
for index in range(len(ints)):
    if(ints[index] in arr.values()):
        hit+=1
    else:
        arr[f"{i%3}"] = ints[index]
        miss+=1
        i+=1
print(arr, "hit:", hit, "miss:", miss)
print("hit ratio: ", hit/(hit+miss))