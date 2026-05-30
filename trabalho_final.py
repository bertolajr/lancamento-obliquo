import numpy as np
from manim import *

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

def calcular_vec_velocidade(v_0, theta):
    t=0.0
    vec_x=v_0*np.cos(np.radians(theta))
    vec_list=[]
    while True:
        vec_y=(v_0*np.sin(np.radians(theta)))-(9.81*t)
        if t>0 and vec_y<(-v_0*np.sin(np.radians(theta))):
            break
        else:
            vec_list.append([vec_x, vec_y])
            t+=0.005
    return vec_list

v_0=float(input("Informe a velocidade inicial (m/s): "))
theta=float(input("Informe o ângulo de lançamento (⁰): "))

class Lancamento(Scene):
    def construct(self):
        pontos_da_trajetoria=calcular_trajetoria(v_0, theta)
        eixos=Axes(
            x_range=[0,30,5],
            y_range=[0,15,5],
            axis_config={"include_tip":True}
        )
        pontos_manim=[eixos.c2p(i[0], i[1]) for i in pontos_da_trajetoria]

        trajetoria=VMobject()
        trajetoria.set_points_as_corners(pontos_manim)

        projetil=Dot(color=BLUE)
        projetil.move_to(pontos_manim[0])

        self.play(Create(eixos))
        self.play(Create(trajetoria), run_time=2)
        self.play(MoveAlongPath(projetil, trajetoria), run_time=2, rate_func=linear)
        self.wait(2)