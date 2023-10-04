
raamatu_riiul = [5,3,7,2,8,4,9]

for i in range(1, len(raamatu_riiul)):
        key = raamatu_riiul[i]
        j = i - 1 
        while j >= 0 and key < raamatu_riiul[j]:
            raamatu_riiul[j+1] = raamatu_riiul[j]
            j -= 1
        raamatu_riiul[j+1] = key

print(raamatu_riiul)
