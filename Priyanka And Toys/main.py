w = [1,2,3,21,7,12,14,21]
n = len(w)

arr = sorted(w)
cont_count = 1
cont_min_weight = arr[0]

for i in arr[1:]:
    if i <= cont_min_weight + 4:
        # can be added to existing container
        continue
    else:
        cont_min_weight = i
        cont_count += 1

print(cont_count)
