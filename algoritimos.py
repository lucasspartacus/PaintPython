"""
//Lucas Spartacus Vieira Carvalho (655455)
//curso de ciencia da computação  
//Projeto 1
//Computação gráfica 

"""

"""
Implementação dos algoritmos vistos em sala
"""
from math import *
"""
Algoritmo DDA(Analisador diferencial digital)
O algoritmo sempre escolhendo o maior entre Δx e Δy
Sempre usa valores arredondados para que não haja distorção no pixel
Caso 1(Δx>Δy): m=2Δy/Δx e x soma 1 constante, repete Δx vezes
Caso 2(Δy>Δx): m=2Δx/Δy e y some 1 constante, repete Δy vezes
A partir de um ponto, encontra-se o próximo somando o produto de uma constante K por Δy e Δx, 
respectivamente às coordenadas x e y desse ponto.
 
"""
def dda(px1, py1, cor): 
    x, y = px1['x'], px1['y']
    dx = py1['x'] - x
    dy = py1['y'] - y
    set_pixel = [px1]

    if abs(dx) > abs(dy) : #1° caso
        passos = int(abs(dx))
    else:#2° caso
        passos = int(abs(dy))

    if passos == 0:
        return set_pixel

    xincr = dx/passos
    yincr = dy/passos
    
    for K in range(passos):#encontra todos os pontos da reta dda
        x += xincr
        y += yincr
        set_pixel.append({'x': round(x), 'y': round(y)})

    return set_pixel

"""
O algoritmo de Bresenham para retas apenas realiza cálculos com inteiros.
Substitui-se a inclinação pelo quociente Δy/ Δx, o que leva a utilização de apenas operações inteiras.
Obtém-se a variável de decisão  p=2Δy*xant - 2Δx*yant +c, podendo assim calcular p de forma incremental. Usando as seguintes forma no algoritmo:
Caso 1(Δx>Δy): p=Δy-Δx,  c1= 2Δy, c2 = 2Δy
Caso 2(Δy>Δx): p=2Δx-Δy,  c1= 2Δx, c2 = 2(Δx-Δy)
 
"""

def alg_bresenham(px1, py1, cor):
    x, y = px1['x'], px1['y']
    dx = int(py1['x'] - x)
    dy = int(py1['y'] - y)
    colora_pixel = [px1]

    if dx >= 0 :
       xincr = 1
    else: 
        xincr = -1; dx = -dx 

    if dy >= 0 : 
        yincr = 1
    else: 
        dy = -dy
        yincr = -1
        
        
    if dx > dy : #1° caso
        p = 2*dy-dx
        const1 = 2*dy; const2 = 2*(dy-dx)
        for i in range(dx):#encontra todos os pontos da reta Bresenhan do primeiro caso
            x += xincr  #sempre atualiza x
            if p < 0 :
                p+= const1
            else: 
                y += yincr
                p+= const2
            colora_pixel.append({'x': x, 'y': y})
    else: #2° caso
        p = 2*dx-dy; const1 = 2*dx; const2 = 2*(dx-dy)
        for i in range(dy):#encontra todos os pontos da reta Bresenhan do segundo caso
            y += yincr #sempre atualiza y
            if p < 0 :
                p += const1
            else:
                p += const2
                x += xincr            
            colora_pixel.append({'x': x, 'y': y})
    return colora_pixel

"""
O algoritmo de Bresenhan para circunferência apenas realiza cálculos com inteiros.
Considera cálculos de uma circunferência na origem e aplica translação   x²+y²=r²
Calcula somente 1 octante sendo ele o 2° tendo assim x=0 e y=raio e calcula os outros octantes por simetria
Repete enquanto x for menor que Y
se P < 0, faz p=p+4x+6
se P>= 0, faz p=p+4(x-y)10, y=y-1

"""
def circunferenciaBresenhan(C, px1, cor):
    raio = round(sqrt((C['x'] - px1['x'])**2 +(C['y'] - px1['y'])**2))
    x = 0
    y = raio
    p = 3 - 2 * raio
    circulo = plot_circle_points(C, x, y)
    while x < y:
        if p < 0:
            p += 4 * x + 6
        else:
            p += 4 * (x - y) + 10
            y -= 1
        x += 1
        circulo += plot_circle_points(C,x,y)
    return circulo

"""
Realiza a translação inversa em todos os simétricos de cada ponto (x,y) encontrado pelo algoritmo 
de circunferência de Bresenham

"""
def plot_circle_points(C, x, y):
    pontos = []
    pontos.append({'x': C['x'] + x, 'y': C['y'] + y})
    pontos.append({'x': C['x'] + x, 'y': C['y'] - y})
    pontos.append({'x': C['x'] - x, 'y': C['y'] + y})
    pontos.append({'x': C['x'] - x, 'y': C['y'] - y})
    pontos.append({'x': C['x'] + y, 'y': C['y'] + x})
    pontos.append({'x': C['x'] + y, 'y': C['y'] - x})
    pontos.append({'x': C['x'] - y, 'y': C['y'] + x})
    pontos.append({'x': C['x'] - y, 'y': C['y'] - x})
    return pontos


""""
Regiões codificadas
O algoritmo de sutherland faz codificação da localização relativa dos extremos do segmento de reta em relação à janela.
O algoritmo de sutherland faz a verificação de localização verificando se ambos os extremos possuem código zero, 
O segmento está completamente dentro da janela ou se ambos os extremos possuem um bit 1 na mesma posição, o segmento está completamente fora da janela.
se não o segmento está parcialmente dentro da janela, tendo assim que realizar os cálculos que verifica se os pontos são maiores ou menores do que xmax, xmin, ymax, ymin
verificando assim os partes que não serão visíveis no recorte

"""
def cohenSutherland(px1, py1, px2, py2):
    aceito = False
    feito = False
    (xmax, ymax, xmin, ymin) = limites(px1, py1)
    (x1, y1, x2, y2) = (px2['x'], px2['y'], py2['x'], py2['y'])
    
    #repete enquanto ainda tiver calculos a serem feitos
    while not feito:
        c1 = region_code(px1, py1, x1, y1)
        c2 = region_code(px1, py1, x2, y2)
        #otimização de calculo
        if c1 == 0 and c2 == 0:  #completamente dentro da janela
            aceito = True
            feito  = True
        elif c1 & c2 != 0: #completamente fora da janela, verifica se bit resultate de cod1 & cod é diferente de  0  
            feito  = True
        else:
            if c1 != 0:#determina um ponto exterior
                cfora = c1
            else:
                cfora = c2

            if cfora & 1 == 1: #se bit 0 está setado
                xint = xmin
                yint = y1 + (y2-y1) * (xmin-x1)/ (x2-x1)
            elif cfora & 2 == 2: #se bit 1 está setado
                xint = xmax
                yint = y1 + (y2-y1) * (xmax-x1)/(x2-x1)
            elif cfora & 4 == 4: #se bit 2 está setado
                yint = ymin
                xint = x1 + (x2-x1) * (ymin-y1)/(y2-y1)
            elif cfora & 8 == 8: #se bit 3 está setado
                yint = ymax
                xint = x1 + (x2-x1) * (ymax-y1)/(y2-y1)

            if cfora == c1: #atualiza ponto incial da reta
                x1 = xint
                y1 = yint
            else:             #atualiza ponto final da reta
                x2 = xint
                y2 = yint
    if(aceito):
        return (round(x1), round(y1), round(x2), round(y2))
    else:
        return ()

"""
Para cada ponto extremo P=(x,y)gera-se o código ativando os respectivos bits, setando a região determinada
"""

def region_code(px1, py1, x, y):
    cod = 0
    (xmax, ymax, xmin, ymin) = limites(px1, py1)
    if x < xmin:  #seta bit 0
        cod +=1
    elif x > xmax:  #seta bit 1
        cod += 2

    if y < ymin:  #seta bit 2
        cod += 4
    elif y > ymax:  #seta bit 3
        cod += 8

    return cod

"""
seta os limetes da janela 

"""
def limites(px1, py1):
    if px1['x'] > py1['x']:
        xmax = px1['x']
        xmin = py1['x']
    else:
        xmax = py1['x']
        xmin = px1['x']

    if px1['y'] > py1['y']:
        ymax = px1['y']
        ymin = py1['y']
    else:
        ymax = py1['y']
        ymin = px1['y']
    
    return(xmax, ymax, xmin, ymin)

"""
Equação paramétrica
O algoritmo liang-Barsky utiliza da equação paramétrica da reta,
Variando u de 0 a 1 obtêm-se todos os pontos do segmento de reta de px1 a py1 
Para cada PK(sendo < > = ou ≠ vai representar a posição da linha)
Para cada segmento de reta, calculam-se os valores de u1 e u2, que definem a parte da reta interior à janela
Passa obrigatoriamente pelas 4 fronteiras.

"""   

def liangBarsky(px1, py1, px2, py2):
    u1 = 0.0
    u2 = 1.0

    (x1, y1, x2, y2) = (px2['x'], px2['y'], py2['x'], py2['y'])
    (xmax, ymax, xmin, ymin) = limites(px1, py1)

    dx = x2 - x1
    dy = y2 - y1
    
    u1, u2, result = cliptest(-dx, x1 - xmin, u1, u2)
    if result: #fronteira esquerda
        u1, u2, result = cliptest(dx, xmax - x1, u1, u2)
        if result: #fronteira direita
            u1, u2, result = cliptest(-dy, y1 - ymin, u1, u2)
            if result: #fronteira inferior
                u1, u2, result = cliptest(dy, ymax - y1, u1, u2)
                if result: #fronteira superior
                    if u2 < 1.0:
                        x2 = x1 + (dx * u2) # x1 = valor inicial antes do recorte
                        y2 = y1 + (dy * u2) # y1 = valor inicial antes do recorte
                    if u1 > 0.0:
                        x1 = x1 + (dx * u1)
                        y1 = y1 + (dy * u1)
                    return (round(x1), round(y1), round(x2), round(y2))

    return ()
"""
False = fora da janela, True = dentro da janela

"""

def cliptest(p, q, u1, u2):
    result = True
    if p < 0.0:
        r = q/p
        if r > u2:
            result = False 
        elif r > u1:
            u1 = r
    elif p > 0.0:
        r = q/p
        if r < u1:
            result = False 
        elif r < u2:
            u2 = r
    elif q < 0.0:
        result = False
    return (u1, u2, result) 
