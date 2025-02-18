# Calculate perimeter and area of shapes such as triangle, rectangle, square and circle when no. side inputted by 3, 2, and 1 resp.
num_side = int(input('Enter no. of sides (2 for rectange), (3 for triangle), (1 for square/circle): '))

if num_side ==3:
    # Triangle
    side1 = float(input('Enter side 1: '))
    side2 = float(input('Enter side 2: '))
    side3 = float(input('Enter side 3: '))
    p = side1 + side2 + side3
    ar = (p/2*(p/2-side1)*(p/2-side2)*(p/2-side3))**0.5
    print(f'Area {ar} and Perimeter {p} of given Triangle with sides {side1}, {side2}, {side3}')

elif num_side ==2:
    # rectangle
    l = float(input('Enter lenght: '))
    b = float(input("Enter breadth: "))
    p = 2*(l+b)
    ar = l*b
    print(f'Perimeter: {p} and Area : {ar} of given Rectangle with length {l} and with breadth {b}')


    # square or circle
elif num_side == 1:
        shape = input("Enter shape (square/circle): ")
        if shape.lower()== 'Square':
            side = float(input('Enter side: '))
            p = 4*side
            ar = side**2
            print(f'Perimeter {p} and area {ar} of given square')
        elif shape.lower() == 'circle':
            r = float(input("Enter radius: "))
            c = 2*3.14*r
            ar = 3.14*r**2
            print(f'Circumference: {c} and Area : {ar}')
        else:
            print("Invalid input!")
else:
     print("Invalid input!")