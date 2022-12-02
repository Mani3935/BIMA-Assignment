

# Input of points
n = int(input("Enter number of Polygon Points:  "))

# Number of points restriction

while n < 3:
    print ("Number of points should be greater than 2 to make a polygon!")
    n = int(input("Enter again number of Polygon Points:  "))
    if n > 2:
        break


print()

# Input of Coordinate points

Xa = []
Ya = []

for i in range (n):
    x , y = (input("enter value for 'x' ˽ 'y' coordinates:  " )).split()
    Xa.append(x)
    Ya.append(y)


print()
print()
print(f"{'Points' :>0} {'x' :>15} {'y' :>20}")
print("-" * 45)

for i in range (n):
    print(f"{i + 1:>3} {Xa[i]:>18} {Ya[i]:>20}")

print()
print()


# Initial Values

# Area
A = 0 
# Static Moment X
Sx = 0
# Static Moment Y
Sy = 0
# Moment of Inertia X
Ix = 0
# Moment of Inertia Y
Iy = 0
# Moment of Inertia XY
Ixy = 0

# Execution of the formulas

for g in range (n):
    Xi = int (Xa [g-1])
    Xi1 = int (Xa [g])
    Yi = int (Ya [g-1])
    Yi1 = int (Ya [g])

    # Formula for Area
    A = A + (Xi1 + Xi) * (Yi1 - Yi)

    # Formula for Static Moment X
    Sx = Sx + (Xi1 - Xi) * (Yi1**2 + Yi*Yi1 + Yi**2)

    # Formula for Static Moment Y
    Sy = Sy + (Yi1 - Yi) * (Xi1**2 + Xi*Xi1 + Xi**2)

    # Formula for Moment of Inertia X
    Ix = Ix + (Xi1 - Xi) * (Yi1**3 + (Yi1**2)*Yi + Yi1*(Yi**2) + Yi**3)

    # Formula for Moment of Inertia Y
    Iy = Iy + (Yi1 - Yi) * (Xi1**3 + (Xi1**2)*Xi + Xi1*(Xi**2) + Xi**3)

    # Formula for Moment of Inertia XY
    Ixy = Ixy + (Yi1 - Yi) * ((Yi1 * (3*Xi1**2 + 2*(Xi1*Xi) + Xi**2)) + Yi * (3*Xi**2 + 2 * (Xi1*Xi) + Xi1**2))

print ()
print ("Geometric Characterictics: ")

A = (1/2) * A

print ('Area: ',"\t","\t","\t",f"{A:.2f}")

Sx = (-1/6) * Sx

print ('Static Moment X: ',"\t",f"{Sx:.2f}")

Sy = (1/6) * Sy

print ('Static Moment Y: ',"\t",f"{Sy:.2f}")

Ix = (-1/12) * Ix

print ('Moment of Inertia X: ',"\t",f"{Ix:.2f}")

Iy = (1/12) * Iy

print ('Moment of Inertia Y: ',"\t",f"{Iy:.2f}")

Ixy = (-1/24) * Ixy

print ('Moment of Inertia XY: ',"\t",f"{Ixy:.2f}")


print ()
print ("Coordinates of Centroid of Corss-Section: ")

Xt = Sy/A

print ('Xt: ',"\t",f"{Xt:.2f}")

Yt = Sx/A

print ('Yt: ',"\t",f"{Yt:.2f}")


print ()
print ("Moments of Inertia w.r.t axes in parallel through the points of gravity of cross-section: ")

Ixt = Ix - (Yt**2 * A)

print ('Ixt: ',"\t",f"{Ixt:.2f}")

Iyt = Iy - (Xt**2 * A)

print ('Iyt: ',"\t",f"{Iyt:.2f}")

Ixyt = Ixy + (Xt * Yt * A)

print ('Ixyt: ',"\t",f"{Ixyt:.2f}")


