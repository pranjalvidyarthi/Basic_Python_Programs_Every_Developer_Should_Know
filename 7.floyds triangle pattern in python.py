def floyds_triangle(rows):
    alphabet = ord('A') # Start from A
    for i in range(1, rows + 1):
        for j in range(i):
            print(chr(alphabet), end="")
            alphabet +=1
            if alphabet > ord('Z'): # Reset if beyond 'Z'
                alphabet = ord('A')
        print()

floyds_triangle(6)