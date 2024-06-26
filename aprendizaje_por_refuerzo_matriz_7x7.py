import numpy as np
import matplotlib.pyplot as plt
from collections import defaultdict
from tqdm import tqdm

nx=7
ny=7
acciones={'arriba':[0,1], 'abajo':[0,-1], 'izquierda':[-1,0], 'derecha':[1,0]}
acc=['arriba','abajo','izquierda','derecha']
IndAcc={a:i for a,i in zip(acc, range(4))}
Q=defaultdict(lambda: {a:0 for a in acc})
#Estados con reward especial
# Estados con reward especial
rw = {(x, y): 10 for x in range(nx+1) for y in range(ny+1)}
rw[(6, 6)] = 500
penalized_states = [(0, 3), (0, 4), (0, 5), (0, 6), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                    (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (6, 0), (6, 1)]
penalty = -50

for state in penalized_states:
    rw[state] = penalty

endSt = [(nx, ny)]
alfa=0.9
gamma=0.8
Niter=50000
Eo=1
ef=0.01
k=np.power(ef/Eo,1/Niter)
eps=Eo
for i in tqdm(range(Niter)):
  eps*=k
  #Inicio en estado aleatorio
  s=(0,0)
  N=50 #Número máximo de pasos
  fin=False
  #print('')
  while(N>0 and not(fin)):
    #Determinación si la acción es aleatoria u óptima
    N-=1
    #print(N,fin, end='')
    #print('State: ',s)
    if(np.random.rand()<eps): #Se hace una acción aleatoria
      a=np.random.choice(acc)
    else:
      a=max(Q[s], key=Q[s].get)
    dx,dy=acciones[a] #Cambio en la coordenada del estado según la acción
    #print('Accion: ',a)
    #Revisión de los rebotes en las regiones
    x,y=s
    xn=x+dx
    yn=y+dy
    rwrd=-1
    fin=False
    if(xn>nx or xn<0 or yn>ny or yn<0):
      #Existe un choque con un borde
      rwrd=-10
      xn=xn-dx #Se devuelve el movimiento
      yn=yn-dy
    if((xn,yn) in rw.keys()):
      rwrd=rw[(xn,yn)]
    if((xn,yn) in endSt):
      fin=True
    newSt=(xn, yn)
    Q[s][a]=Q[s][a]+alfa*(rwrd+gamma*max(Q[newSt].values())-Q[s][a])
    s=newSt
#print('Nuevo estado: ',s,'N:',N,'fin: ',fin)
 #Obtener política óptima desde la posición (0, 0)
#pol_optima = max(Q[(0, 0)], key=Q[(0, 0)].get)

#print("La acción óptima desde la posición (0, 0) es:", pol_optima)

#Dibujado de las zonas penalizadas
mx=np.zeros((nx+1, ny+1))
my=np.zeros((nx+1, ny+1))
mreg=np.zeros((nx+1, ny+1))
mV=np.zeros((nx+1, ny+1))
for x in range(nx+1):
  for y in range(ny+1):
    mx[x,y]=x
    my[x,y]=y
    if((x,y) in rw.keys()):
      mreg[x,y]=rw[(x,y)]
    mV[x,y]=max(Q[(x,y)].values())
plt.figure(figsize=(16,8))
plt.subplot(1,2,1)
plt.contourf(mx,my,mreg,50)
plt.colorbar()
plt.axis('equal')
plt.subplot(1,2,2)
plt.contourf(mx,my,mV,50)
plt.colorbar()

for x in range(nx+1):
  for y in range(ny+1):
    vec=list(Q[(x,y)].values())
    mov=acciones[acc[np.argmax(vec)]]
    k=0.4
    plt.arrow(x,y,k*mov[0], k*mov[1], head_width=0.3)
    plt.plot(x,y,'.k')
for k,v in rw.items():
  xi,yi=k
  if(v<0):
    plt.plot(xi,yi, 'xr')
plt.axis('equal')
