import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation,FFMpegWriter

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(projection='3d',computed_zorder=False)

phi1 = np.linspace(0, 2*np.pi, 50)
phi2 = np.linspace(0, 2*np.pi, 50)

P1, P2 = np.meshgrid(phi1, phi2)
r=1
R=2

Z = ((R**2 - 1)**2)

def Phix(p1,p2):
    return (R+r*np.sin(p1))*np.cos(p2)

def Phiy(p1,p2):
    return (R+r*np.sin(p1))*np.sin(p2)

def Phiz(p1,p2):
    return r*np.cos(p1)

def Phi(p1,p2):
    return Phix(p1,p2), Phiy(p1,p2), Phiz(p1,p2)

X,Y,Z = Phi(P1,P2)

a = np.sqrt(2)*np.pi/50

def alpha(p1,p2):
    return p1+a, p1+p2

xlen = len(X)
ylen = len(Y)
colortuple = ('y', 'b')
colors = np.empty(X.shape, dtype=str)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
# Plot the surface.
ax.plot_surface(X, Y, Z, antialiased = False,facecolors=colors,zorder=1)

p10, p20 = (0.0,3/2*np.pi)
x0, y0 , z0 =  Phi(p10,p20)
print(x0,y0,z0)

ax.set_zlim(-3, 3)
ax.set_xlim(-3,3)
ax.set_ylim(-3,3)
ax.set_xlabel(r'$x$-axis')
ax.set_ylabel(r'$y$-axis')
ax.set_zlabel(r'$z$-axis')
#plt.tight_layout()
p1 = 0.0
p2 = 3/2*np.pi
p1s = [p1]
p2s = [p2]
#fig.tight_layout()
plt.tight_layout()

def inif():
    ax.scatter(Phix(p1,p2),Phiy(p1,p2),Phiz(p1,p2), s=10,c = "red",zorder =4, label ="point")
    plt.legend()

def update(frame):
    p1 = p1s[frame]
    p2 = p2s[frame]
    p1n,p2n = alpha(p1,p2)
    p1s.append(p1n)
    p2s.append(p2n)
    x,y,z = Phi(p1,p2)
    print("framenr:")
    print(frame)
    print("pointcoords:")
    print(x,y,z)
    ax.scatter(x,y,z, s=10,c = "red",zorder =4)
    plt.title(str(frame))

ani = FuncAnimation(fig, update,init_func=inif, frames=20,interval = 1000)
writervideo = FFMpegWriter(fps=1)
ani.save("test.mp4", writer=writervideo,dpi=200)
plt.close()
