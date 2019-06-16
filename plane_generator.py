'''
Programa desenvolvido por: Lucas Gabriel de Araujo Silva - 1º Semestre
NºUSP: 11218880
Curso: Ciências da Computação - USP
Matéria: Geometria Analítica
Professor: Ali Tahzibi
Código da matéria: SMA0300
Descrição: Programa que faz o gráfico de 3 planos e sua intersecção.
Data de desenvolvimento: 25 - 27 de abril de 2019
'''

'''
Manual de Uso
Quando rodar o programa digite as 3 equações iniciais no console do python
e o delimitador que é a escala do gráfico 3d.
Após isso será gerado o grafico.
Pode-se alterar as equações a qualquer momento nas input box que tem na tela,
basta dar o enter após colocar os 4 numeros em uma input box. Também pode mudar o
delimitador.
Ao clicar nas legendas você pode ocultar/mostrar os elementos do gráfico.
Para usar o programa deve ter os seguintes módulos Python:
- numpy
- sympy
- matplotlib
'''

import numpy as np
import sympy as sp
from sympy import Eq, solve_linear_system, Matrix
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.widgets import TextBox
from mpl_toolkits.mplot3d import Axes3D


#CASOS DE TESTE
##TEMPLATE row1=equação1=[a,b,c,-d]
#T1:Resolvível deu certo
#row1 = [1,2,-1,-6]
#row2 = [3,1,1,4]
#row3 = [1,-3,-2,1]
#T2:Indeterminado deu certo
#row1 = [1,2,-3,-6]
#row2 = [2,-1,-1,3]
#row3 = [1,1,-2,-3]
#Indeterminado igual deu certo
#row1 = [1,2,-3,-6]
#row2 = [2,4,-6,-12]
#row3 = [-1,-2,3,6]
#Impossível deu certo, retorna none
#row1 = [1,2,-3,-6]
#row2 = [1,2,-3,0]
#row3 = [1,2,-3,5]
#Impossível deu certo
#row1 = [1,2,-3,-6]
#row2 = [-1,-2,3,0]
#row3 = [2,1,-3,2]
#Impossível deu certo
#row1 = [1,1,1,6]
#row2 = [2,-1,0,-1]
#row3 = [3,0,1,2]

delim = 10000

def get_plane(a,b,c,d):
    x = np.linspace(-delim,delim,10)
    y = np.linspace(-delim,delim,10)
    z = np.linspace(-delim,delim,10)
    if(a != 0):
        Z,Y = np.meshgrid(z,y)
        X = (-d -(b*Y) - (c*Z))/a
    elif(b != 0):
        X,Z = np.meshgrid(x,z)
        Y = (-d -(a*X) - (c*Z))/b
    elif(c != 0):
        X,Y = np.meshgrid(x,y)
        Z = (-d -(a*X) - (b*Y))/c
    return X,Y,Z

def get_line(ans,eq1,eq2,eq3):
    x,y,z = sp.symbols('x y z')
    dem = np.linspace(-delim,delim,10)
    X = []
    Y = []
    Z = []
    system = Matrix((eq1,eq2,eq3))
    t1,t2,t3 = False,False,False
    for a in ans:
        if(a == x):
            t1 = True
        if(a == y):
            t2 = True
        if(a == z):
            t3 = True
    if(t1 == False): 
        #print("em função de x")
        for a in dem:
            x,y,z = sp.symbols('x y z')
            x=a
            sol = solve_linear_system(system,x,y,z,dict=True)
            X = X + [a]
            Y = Y + [float(sol[y])]
            Z = Z + [float(sol[z])]
    elif(t2 == False):
        #print("em função de y")
        for a in dem:
            x,y,z = sp.symbols('x y z')
            y=a
            sol = solve_linear_system(system,x,y,z,dict=True)
            X = X + [float(sol[x])]
            Y = Y + [a]
            Z = Z + [float(sol[z])]
    elif(t3 == False):
        #print("em função de z")
        for a in dem:
            x,y,z = sp.symbols('x y z')
            z=a
            sol = solve_linear_system(system,x,y,z,dict=True)
            X = X + [float(sol[x])]
            Y = Y + [float(sol[y])]
            Z = Z + [a]
    return X,Y,Z

def resolve(eq1,eq2,eq3):
    x,y,z = sp.symbols('x y z')
    system = Matrix((eq1,eq2,eq3))
    sol = solve_linear_system(system,x,y,z,dict=True)
    return sol

def onpick(event):
    vis = None
    legline = event.artist
    origline = lined[legline]
    if(origline == fake1):
        vis = not surf1.get_visible()
        surf1.set_visible(vis)
    elif(origline == fake2):
        vis = not surf2.get_visible()
        surf2.set_visible(vis)
    elif(origline == fake3):
        vis = not surf3.get_visible()
        surf3.set_visible(vis)
    elif(origline == fake4):
        vis = not in1.get_visible()
        in1.set_visible(vis)
    if vis:
        legline.set_alpha(1.0)
    else:
        legline.set_alpha(0.2)
    fig.canvas.draw()

def submit1(text):
    global surf1
    global eq1
    global initial_text1
    initial_text1 = text
    nums = text.split(" ")
    a,b,c,d = float(nums[0]),float(nums[1]),float(nums[2]),float(nums[3])
    eq1 = [a,b,c,-d]
    surf1.remove()
    X,Y,Z = get_plane(a,b,c,d)
    surf1 = ax.plot_surface(X, Y, Z,color='blue', alpha= 0.5,linewidth=0,zorder=-1, shade=False)
    redrawinter()
    plt.draw()
    return None
def submit2(text):
    global surf2
    global eq2
    global initial_text2
    initial_text2 = text
    nums = text.split(" ")
    a,b,c,d = float(nums[0]),float(nums[1]),float(nums[2]),float(nums[3])
    eq2 = [a,b,c,-d]
    surf2.remove()
    X,Y,Z = get_plane(a,b,c,d)
    surf2 = ax.plot_surface(X, Y, Z,color='green', alpha= 0.8,linewidth=0,zorder=0, shade=False)
    redrawinter()
    plt.draw()
    return None
def submit3(text):
    global surf3
    global eq3
    global initial_text3
    initial_text3 = text
    nums = text.split(" ")
    a,b,c,d = float(nums[0]),float(nums[1]),float(nums[2]),float(nums[3])
    eq3 = [a,b,c,-d]
    surf3.remove()
    X,Y,Z = get_plane(a,b,c,d)
    surf3 = ax.plot_surface(X, Y, Z,color='yellow', alpha= 0.8,linewidth=0,zorder=1, shade=False)
    redrawinter()
    plt.draw()
    return None
def submit4(text):
    global delim
    global ax
    global initial_text1
    global initial_text2
    global initial_text3
    delim = int(text)
    ax.set_xlim(-delim,delim)
    ax.set_ylim(-delim,delim)
    ax.set_zlim(-delim,delim)
    submit1(initial_text1)
    submit2(initial_text2)
    submit3(initial_text3)
    
def redrawinter():
    global eq1
    global eq2
    global eq3
    global in1
    ans = resolve(eq1,eq2,eq3)
    if(ans != None):
        if(len(ans)==3):
            in1.remove()
            p1 = int(ans[x])
            p2 = int(ans[y])
            p3 = int(ans[z])
            print("Ponto de Interseção: ")
            print(ans)
            in1, = ax.plot([p1],[p2],[p3],label='Interseção', color='r',marker='o',alpha=1,zorder=5)
        elif(len(ans)==2):
            in1.remove()
            print("Reta de Interseção: ")
            print(ans)
            X,Y,Z = get_line(ans,eq1,eq2,eq3)
            in1, = ax.plot(X,Y,Z,label='Interseção',color='red',zorder=5)
        else:
            print("Não há Interseção entre os planos.")
            in1.set_alpha(0.0)
    else:
        print("Não há Interseção entre os planos.")
        in1.set_alpha(0.0)
        
#a1,b1,c1,d1 = 1,2,-3,6
#a2,b2,c2,d2 = 2,-1,-1,-3
#a3,b3,c3,d3 = 1,1,-2,3
num1 = input("Entre a equação do 1º plano (digite apenas os valores de a,b,c,d)(ax+by+cz+d = 0):").split(" ")
num2 = input("Entre a equação do 2º plano (digite apenas os valores de a,b,c,d)(ax+by+cz+d = 0):").split(" ")
num3 = input("Entre a equação do 3º plano (digite apenas os valores de a,b,c,d)(ax+by+cz+d = 0):").split(" ")
a1,b1,c1,d1 = float(num1[0]),float(num1[1]),float(num1[2]),float(num1[3])
a2,b2,c2,d2 = float(num2[0]),float(num2[1]),float(num2[2]),float(num2[3])
a3,b3,c3,d3 = float(num3[0]),float(num3[1]),float(num3[2]),float(num3[3])
num4 = input("Selecione o delimitador(escala maior ou menor):")
delim = int(num4)
X1,Y1,Z1 = get_plane(a1,b1,c1,d1)
X2,Y2,Z2 = get_plane(a2,b2,c2,d2)
X3,Y3,Z3 = get_plane(a3,b3,c3,d3)

x,y,z = sp.symbols('x y z')
eq1 = None
eq2 = None
eq3 = None
eq1 = [a1,b1,c1,-d1]
eq2 = [a2,b2,c2,-d2]
eq3 = [a3,b3,c3,-d3]
ans = resolve(eq1,eq2,eq3)

fig = plt.figure("Simulador de Planos",figsize=(6,6))
ax = fig.add_subplot(111, projection='3d')
#ax.set_xlabel("X")
#ax.set_ylabel("Y")
#ax.set_zlabel("Z")
#ax.set_xticklabels("")
#ax.set_yticklabels("")
#ax.set_zticklabels("")
ax.set_xlim(-delim,delim)
ax.set_ylim(-delim,delim)
ax.set_zlim(-delim,delim)
#ax.set_xlim(max(a1,a2,a3)*(-delim),max(a1,a2,a3)*(delim))
#ax.set_ylim(max(b1,b2,b3)*(-delim),max(b1,b2,b3)*(delim))
#ax.set_zlim(max(c1,c2,c3)*(-delim),max(c1,c2,c3)*(delim))
ax.set_axis_off()
surf1 = None
surf2 = None
surf3 = None
in1 = None
if(ans != None):
    if(len(ans)==3):
        p1 = int(ans[x])
        p2 = int(ans[y])
        p3 = int(ans[z])
        print("Ponto de Interseção: ")
        print(ans)
        in1, = ax.plot([p1],[p2],[p3], color='r',marker='o',alpha=1,zorder=5)
    elif(len(ans)==2):
        print("Reta de Interseção: ")
        print(ans)
        X,Y,Z = get_line(ans,eq1,eq2,eq3)
        in1, = ax.plot(X,Y,Z,color='red',zorder=5)
    else:
        print("Não há Interseção entre os planos.")
else:
    print("Não há Interseção entre os planos.")
surf1 = ax.plot_surface(X1, Y1, Z1,color='blue', alpha= 0.5,linewidth=0,zorder=-1, shade=False)
surf2 = ax.plot_surface(X2, Y2, Z2,color='green', alpha= 0.8,linewidth=0,zorder=0, shade=False)
surf3 = ax.plot_surface(X3, Y3, Z3,color='yellow', alpha= 0.8,linewidth=0,zorder=1, shade=False)
fake4, = ax.plot([0],[0],label='Interseção',color='red',marker='o')
fake1, = ax.plot([0],[0],label='1ºPlano',color='blue',marker='o')
fake2, = ax.plot([0],[0],label='2ºPlano',color='green',marker='o')
fake3, = ax.plot([0],[0],label='3ºPlano',color='yellow',marker='o')
fake1.set_alpha(0.0)
fake2.set_alpha(0.0)
fake3.set_alpha(0.0)
fake4.set_alpha(0.0)
leg = ax.legend(loc='upper left', fancybox=True, shadow=True)
leg.get_frame().set_alpha(0.4)
lines = [fake4,fake1,fake2,fake3]
lined = dict()
for legline, origline in zip(leg.get_lines(), lines):
    legline.set_picker(5)
    legline.set_alpha(1.0)
    lined[legline] = origline

initial_text1 = str(a1) + ' ' + str(b1) + ' ' + str(c1) + ' ' + str(d1)
initial_text2 = str(a2) + ' ' + str(b2) + ' ' + str(c2) + ' ' + str(d2)
initial_text3 = str(a3) + ' ' + str(b3) + ' ' + str(c3) + ' ' + str(d3)
initial_text4 = str(delim)
axbox1 = plt.axes([0.2,0.15,0.4,0.06])
axbox2 = plt.axes([0.2,0.08,0.4,0.06])
axbox3 = plt.axes([0.2,0.001,0.4,0.06])
axbox4 = plt.axes([0.75,0.15,0.2,0.06])
text_box1 = TextBox(axbox1, 'Equação 1º Plano:',initial=initial_text1)
text_box1.on_submit(submit1)
text_box2 = TextBox(axbox2, 'Equação 2º Plano:',initial=initial_text2)
text_box2.on_submit(submit2)
text_box3 = TextBox(axbox3, 'Equação 3º Plano:',initial=initial_text3)
text_box3.on_submit(submit3)
text_box4 = TextBox(axbox4, 'Delimitador',initial=initial_text4)
text_box4.on_submit(submit4)

fig.canvas.mpl_connect('pick_event', onpick)
plt.show()
    
