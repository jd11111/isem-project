import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from matplotlib.animation import FuncAnimation,FFMpegWriter

fig = plt.figure(figsize=(9,8))
ax = fig.add_subplot(projection='3d',computed_zorder=False)

mpl.rc('text',usetex=True)
#font = {"size":30}
#mpl.rc('font',**font)

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
    return r*np.cos(p1)+1.5

def Phi(p1,p2):
    return Phix(p1,p2), Phiy(p1,p2), Phiz(p1,p2)

X,Y,Z = Phi(P1,P2)

a = np.sqrt(2)*np.pi/50

def alpha(p1,p2):
    return p1+a, p1+p2

xlen = len(X)
ylen = len(Y)
colortuple = ((0.75,0.75,0.75), (0.95,0.95,0.95))
colors = np.empty(X.shape, dtype=tuple)
for y in range(ylen):
    for x in range(xlen):
        colors[y, x] = colortuple[(x + y) % len(colortuple)]
# Plot the surface.
print(colors)
ax.plot_surface(X, Y, Z, antialiased = False,facecolors=colors,zorder=1)

p10, p20 = (0.0,3/2*np.pi)
x0, y0 , z0 =  Phi(p10,p20)

lim= 2.5
ax.set_zlim(-lim,lim)
ax.set_xlim(-lim,lim)
ax.set_ylim(-lim,lim)
ax.set_xlabel(r'$x$-axis')
ax.set_ylabel(r'$y$-axis')
ax.set_zlabel(r'$z$-axis')
p1 = 0.0
p2 = 3/2*np.pi
p1s = [p1]
p2s = [p2]
xs = []
#fig.tight_layout()
plt.tight_layout(pad=0.0)
textoffsets =[]

#fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
#x,y,z = Phi(p1,p2)


#ax.scatter(x,y,z, s=30,c = "red",zorder =5, label =r"$\alpha^t (3/2 \pi , 0)$")
#ax.text(x,y,z,"0", zorder=4, color="yellow", size=20, label = "t")
XS = []
YS = []
ZS = []
for j in range(10):
    print(j)
    p1 = p1s[j]
    p2 = p2s[j]
    p1n,p2n = alpha(p1,p2)
    p1s.append(p1n)
    p2s.append(p2n)
    x,y,z = Phi(p1,p2)
    print(x,y,z)
    XS.append(x)
    YS.append(y)
    ZS.append(z)


sc = ax.scatter(XS,YS,ZS, s=30,c = "red",zorder =5)
sc2 = ax.scatter(R*np.cos(p2s),R*np.sin(p2s),-2.5, s=30,c = "black",zorder =5)
sc3 = ax.scatter(r*np.cos(p1s),r*np.sin(p1s),-2.5, s=30,c = "black",zorder =5)

Thetas = np.linspace(0,2*np.pi)
ax.plot(r*np.cos(Thetas), r*np.sin(Thetas),-2.5)
ax.plot(R*np.cos(Thetas), R*np.sin(Thetas),-2.5)

for j in range(len(XS)):
    if j==0:
        x_offset = 0.0
        y_offset = 0.0
        z_offset = 0.05
    elif j==1:
        x_offset = -0.15
        y_offset = -0.15
        z_offset = -0.1
    elif j==8:
        x_offset = -0.1
        y_offset = -0.1
        z_offset -0.1
    elif j==9:
        x_offset = -0.1
        y_offset = -0.1
        z_offset -0.1
    else:
        x_offset =0.05
        y_offset =0.0
        z_offset =-0.3
    ax.text(XS[j]+x_offset,YS[j]+y_offset,ZS[j]+z_offset,str(j), zorder=4, color="yellow", size=20)

plt.tight_layout(pad=0.0)
custom_lines = mpl.lines.Line2D([0], [0], color="yellow", lw=4)
ax.legend([custom_lines,sc], [r'$t=0, \dots, 9$', r"$t \cdot (0,3/2 \pi)$"], fontsize =20, loc ="upper right",borderpad =0.2,borderaxespad= 0.1)
plt.savefig("test.pdf",dpi=150)
#für Animationen:
""" 
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
"""
