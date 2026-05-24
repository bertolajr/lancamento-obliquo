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
            trajetoria.append(ponto)
            break
        else:
            trajetoria.append(ponto)
            t+=0.1
    return trajetoria

v_0=float(input("Informe a velocidade inicial: "))
theta=float(input("Informe o ângulo de lançamento: "))
trajetoria=calcular_trajetoria(v_0, theta)

for x,y in trajetoria:
    print(f"{x:.1f}, {y:.1f}")