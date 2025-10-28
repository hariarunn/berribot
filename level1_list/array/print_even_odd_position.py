list1 = list(map(int, input("Enter the list: ").split()))
even_position = []
odd_position = []

for i in range(len(list1)):
    if i % 2 == 0:
        odd_position.append(list1[i])     
    else:
        even_position.append(list1[i])

print("Even positions:", even_position)
print("Odd positions:", odd_position)
