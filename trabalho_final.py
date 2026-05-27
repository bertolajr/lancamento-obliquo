import numpy as np

def calcular_posicao(t, v_0, theta):
    x=v_0*np.cos(np.radians(theta))*t
    y=(v_0*np.sin(np.radians(theta))*t)-((9.81*(t**2)))/2
    return [x,y]

def calcular_trajetoria(v_0, theta):
    t=0.0
    trajetoria=[]
    while True:
        ponto=calcular_posicao(t, v_0, theta)
        if t>0 and ponto[1]<=0:
            break
        else:
            trajetoria.append(ponto)
            t+=0.005
    return trajetoria


def calcular_x_max(v_0, theta):
    g=9.81
    x_max=((v_0**2)*np.sin(2*np.radians(theta)))/g
    return x_max

def calcular_h_max(v_0, theta):
    g=9.81
    h_max=((v_0*np.sin(np.radians(theta)))**2)/(2*g)
    return h_max

"""
def vec_velocidade():
    return velocidade
"""

v_0=float(input("Informe a velocidade inicial (m/s): "))
theta=float(input("Informe o ângulo de lançamento (⁰): "))
trajetoria=calcular_trajetoria(v_0, theta)
x_max=calcular_x_max(v_0, theta)
h_max=calcular_h_max(v_0, theta)

print("[x, y]")
for i in trajetoria:
    print(f"[{i[0]:.1f}, {i[1]:.1f}]")
print(f"Distância máxima: {x_max:.1f} m")
print(f"Altura máxima: {h_max:.1f} m")