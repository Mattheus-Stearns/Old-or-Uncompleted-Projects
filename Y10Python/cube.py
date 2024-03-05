cube_side = int(input("Please input the length of the side of the cube."))

cube_area = cube_side ** 2 * 6

cube_volume = cube_side ** 3

cube = []

print("The surface area of the cube is:", cube_area, "cm**2")

print("The volume of the cube is:", cube_volume, "cm**3")

cube.append(cube_side)
cube.append(cube_area)
cube.append(cube_volume)

print(cube)