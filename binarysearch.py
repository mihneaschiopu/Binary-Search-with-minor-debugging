nlist = [12, 24, 34, 67, 70, 75, 81, 89, 99]
search_term = 75
found = False

first = 0
last = len(nlist)-1
print(first)
print(last)

while (found == False and first<=last):

    mid = (first+last)//2

    print(mid)

    if (search_term == nlist[mid]):
        found = True
        print('Found item', found)

    elif (search_term > nlist[mid]):
        first = mid + 1

    elif (search_term < nlist[mid]):
        last = mid - 1

print('Out of loop')

if (found):
    print('Your data item has been found')
else:
    print('Your data item has not been found')
