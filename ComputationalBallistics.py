# import libraries
import matplotlib.pyplot as plt
import numpy as np
def BallisticsMath():
    Xmax = int(input("please input desired range (meters)\n"))
    # define constants
    V = 820  # muzzle velocity in meters/ sec
    Area = (2.311 / 100) * np.pi * 2
Drag = (0.759*0.0765)/(12*12*12) *V*V*Area/.04 dt = 0.01
t= 0
x = 0.0
    g = 9.81
    dy = 0
    y=0
    # plot setup
    plt.title("Bullet drop for a given range")
    plt.xlabel("range(meters)")
    plt.ylabel("Difference in y (meters)")
    # Loop
    while V > 0 and x < Xmax:
        a = Drag
        V += a * dt
        x += V * dt
        t += dt
        dy += -g * dt
        y += dy * dt
        plt.scatter(x, y, color='red')
        plt.show(block=False)
        plt.pause(.00001)
    plt.scatter(x, y, color="red")
    plt.show()
    #adjustment angle
    Angle = (np.absolute(y)/Xmax) * (180/ np.pi)
    print(f"Your total drop over {Xmax} meters is {np.absolute(y)} meters")
    print(f"Your adjustment angle is {Angle} degrees")
# main execution
# =====================
if __name__ == "__main__":
    BallisticsMath()
