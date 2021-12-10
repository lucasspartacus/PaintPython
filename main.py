"""
//Lucas Spartacus Vieira Carvalho (655455)
//curso de ciencia da computação  
//Projeto 1
//Computação gráfica 

"""

import sys
from PyQt5.QtGui import*
from algoritimos import*
from math import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
class window(QMainWindow):    
    def __init__(self):
        super().__init__()
        self.linhadda = []
        self.linhabresehan = []
        self.circulosbresehan = []
        self.funcao = '' 
        self.recortar1 = 0
        self.recortar2 = 0
        self.Cwindow()    
           
    """
    Cria a janela de exibição
    Selecion o tamanho na execução
    
    """        
    def Cwindow(self):              
        self.resize(1200, 1000)
        self.setWindowTitle('Projeto 1 - Computação Gráfica')        
        self.setWindowIcon(QIcon('imagens/PUC.png'))   

        """
        cria na toolbar todos os atalhos para realizar as transformações geométrica ou a execução dos algoritmos 
        e demonstração gráfica dos mesmos

        """

        self.toolbar = self.addToolBar('Projeto 1')   
        
        #icone linha DDA
        drawAct = QAction(QIcon('imagens/linha.png'), 'Reta(DDA)', self.toolbar)
        drawAct.triggered.connect(self.LinhaDDA)
        self.toolbar.addAction(drawAct)
        #icone linha Bresenhan
        drawAct = QAction(QIcon('imagens/linha.png'), 'Reta(Bresenhan)', self.toolbar)
        drawAct.triggered.connect(self.Linhabresh)  
        self.toolbar.addAction(drawAct)
        #icone circunferência Bresenhan
        drawAct = QAction(QIcon('imagens/circulo.png'), 'Circulo(Bresenhan)', self.toolbar)
        drawAct.triggered.connect(self.CirculoBresh)  
        self.toolbar.addAction(drawAct)
        #icone trasformação geométrica Traslação
        drawAct = QAction(QIcon('imagens/traslacao.png'), 'Translação', self.toolbar)
        drawAct.triggered.connect(self.TranslacaoMenu)
        self.toolbar.addAction(drawAct)
        #icone trasformação geométrica Escala
        drawAct = QAction(QIcon('imagens/escala.png'), 'Escala', self.toolbar)
        drawAct.triggered.connect(self.EscalaMenu)
        self.toolbar.addAction(drawAct)
        #icone trasformação geométrica rotação
        drawAct = QAction(QIcon('imagens/rotacao.png'), 'Rotação', self.toolbar)
        drawAct.triggered.connect(self.RotacaoMenu)
        self.toolbar.addAction(drawAct)
        #icone trasformação geométrica reflexão na origem
        drawAct = QAction(QIcon('imagens/reflexao.png'), 'Reflexão na origem ', self.toolbar)
        drawAct.triggered.connect(self.reflexaoOrigem)
        self.toolbar.addAction(drawAct)
        #icone trasformação geométrica reflexão em x
        drawAct = QAction(QIcon('imagens/reflexaox.png'), 'Reflexão em X', self.toolbar)
        drawAct.triggered.connect(self.reflexaoX)
        self.toolbar.addAction(drawAct)
        #icone trasformação geométrica reflexão em y
        drawAct = QAction(QIcon('imagens/reflexaoy.png'), 'Reflexão em Y', self.toolbar)
        drawAct.triggered.connect(self.reflexaoY)
        self.toolbar.addAction(drawAct)
        #icone recorte Cohen Sutherland
        drawAct = QAction(QIcon('imagens/recortar.png'), 'Recortar(Cohen Sutherland)', self.toolbar)
        drawAct.triggered.connect(self.RecorteCohen)
        self.toolbar.addAction(drawAct)
        #icone recorte Liang-Barsk
        drawAct = QAction(QIcon('imagens/recortar.png'), 'Recortar(Liang-Barsky)', self.toolbar)
        drawAct.triggered.connect(self.RecorteLiang)
        self.toolbar.addAction(drawAct)
        #icone limpar tela
        drawAct = QAction(QIcon('imagens/limpar.png'), 'Limpar', self.toolbar)
        drawAct.triggered.connect(self.Limpar)
        self.toolbar.addAction(drawAct)

        self.show() 

        """
        verifica em qual ícone o mouse clica no canvas
        
        """    

    def mousePressEvent(self, event):        
        if event.button() == Qt.LeftButton :
            if self.funcao == 'dda':
                ponto1 = {'x': event.pos().x(), 'y': event.pos().y()}
                self.linhadda.append([ponto1,ponto1])
           
            elif self.funcao == 'Bresenhan':            
                ponto1 = {'x': event.pos().x(), 'y': event.pos().y()}
                self.linhabresehan.append([ponto1,ponto1])
      
            elif self.funcao == 'circulo':                            
                ponto1 = {'x': event.pos().x(), 'y': event.pos().y()}
                self.circulosbresehan.append([ponto1,ponto1])
              
            elif self.funcao == 'recortar1':
                self.recortar1 = {'x': event.pos().x(), 'y': event.pos().y()}                
               
            elif self.funcao == 'recortar2':
                self.recortar1 = {'x': event.pos().x(), 'y': event.pos().y()}       

        """
            Verifica a movimentação do mouse para gerar os objetos linhas ou circunferência 
            e também para a realização dos dois recortes 

        """          
  
    def mouseMoveEvent(self, event):
        if self.funcao == 'dda':
            ponto2 = {'x': event.pos().x(), 'y': event.pos().y()}
            self.linhadda[len(self.linhadda) - 1][1] = ponto2
            self.update()
        if self.funcao == 'Bresenhan':
            ponto2 = {'x': event.pos().x(), 'y': event.pos().y()}
            self.linhabresehan[len(self.linhabresehan) - 1][1] = ponto2
            self.update()
        if self.funcao == 'circulo':
            ponto2 = {'x': event.pos().x(), 'y': event.pos().y()}
            self.circulosbresehan[len(self.circulosbresehan) - 1][1] = ponto2
            self.update()
        if self.funcao == 'recortar1':
            self.recortar2 = {'x': event.pos().x(), 'y': event.pos().y()}
        if self.funcao == 'recortar2':
            self.recortar2 = {'x': event.pos().x(), 'y': event.pos().y()}

    def LinhaDDA(self):
        self.funcao = 'dda'
    
    def Linhabresh(self):
        self.funcao = 'Bresenhan'
    
    def CirculoBresh(self):
        self.funcao = 'circulo'

    def RecorteCohen(self):
        self.funcao = 'recortar1'

    def RecorteLiang(self):
        self.funcao = 'recortar2' 
        
        """
        Realiza todas as transformações geométricas (translação, escala, reflexão e rotação )
        Representação gráfica dos mesmos
        
        """
 
        """
        Realiza a translação (deslocamento/movimentação de um ponto 1 para um ponto 2)
        Recebendo o valor dos ponto e soma a eles o valor de translação
        É feita a translação nos objetos linaDDA, linhaBresehan  e CirculoBresehan
 
        """
    def TranslacaoMenu(self):
        x, y, entrada = TranslacaoMenu.getResults()
        if entrada:               
            for i in self.linhadda:#repete para a traslação todos os pontos da reta
                for ponto in i:
                    ponto['x'] += int(x)
                    ponto['y'] += int(y)
            for i in self.linhabresehan:#repete para a traslação todos os pontos da reta
                for ponto in i:
                    ponto['x'] += int(x)
                    ponto['y'] += int(y)
            for i in self.circulosbresehan:#repete para a traslação todos os pontos da circunferência 
                for ponto in i:
                    ponto['x'] += int(x)
                    ponto['y'] += int(y)

    """
    Realiza a escala(altera as dimensões do objeto)
    Recebendo o valor dos ponto e multiplica a eles o valor de escala
    É feita a escala nos objetos linhaDDA, linhaBresehan  e CirculoBresehan
    para cada ponto (x,y) se torna um novo ponto |x' = x*a
                                                 |y' = y*b 
    """
    def EscalaMenu(self):
        a, b, entrada = EscalaMenu.getResults()       
        if entrada:  
            a = float(a.replace(',','.'))
            b = float(b.replace(',','.'))           
            for i in self.linhadda:#repete para a escala todos os pontos da reta
                pontoinicial = i[0]
                for ponto in i:
                    ponto['x'] = ((ponto['x'] - pontoinicial['x'])*a) + pontoinicial['x']
                    ponto['y'] = ((ponto['y'] - pontoinicial['y'])*a) + pontoinicial['y']
            for i in self.linhabresehan:#repete para a escala todos os pontos da reta
                pontoinicial = i[0]
                for ponto in i:
                    ponto['x'] = ((ponto['x'] - pontoinicial['x'])*a) + pontoinicial['x']
                    ponto['y'] = ((ponto['y'] - pontoinicial['y'])*a) + pontoinicial['y']
            for i in self.circulosbresehan:#repete para a escala todos os pontos da circunferência 
                pontoinicial = i[0]
                for ponto in i:
                    ponto['x'] = ((ponto['x'] - pontoinicial['x'])*a) + pontoinicial['x']
                    ponto['y'] = ((ponto['y'] - pontoinicial['y'])*a) + pontoinicial['y']

    """
    Realiza a rotação(Deslocamento circular de um objeto sobre um ponto)
    Realiza a equação matemática  |  x' = x*cosθ  - ysenθ 
                                  |  y' = x*senθ  + ycosθ 
 
    É feita a rotação nos objetos linhaDDA, linhaBresehan 

    """

    def RotacaoMenu(self):
        angulo, entrada = RotacaoMenu.getResults()
        if entrada:
         
            seno = float('{0:.2f}'.format(sin(angulo)))
            cosseno = float('{0:.2f}'.format(cos(angulo)))
            for i in self.linhadda:#repete  a rotação para todos os pontos da reta
                pontoinicial = i[0]
                for ponto in i:
                    x1 = ((ponto['x'] - pontoinicial['x']) * cosseno)
                    y1 = ((ponto['y'] - pontoinicial['y']) * seno)

                    x2 = ((ponto['x'] - pontoinicial['x']) * seno)
                    y2 = ((ponto['y'] - pontoinicial['y']) * cosseno)

                    ponto['x'] = x1 - y1 + pontoinicial['x']
                    ponto['y'] = x2 + y2 + pontoinicial['y']

            for i in self.linhabresehan:#repete a rotação para todos os pontos da reta
                pontoinicial = i[0]
                for ponto in i:
                    x1 = ((ponto['x'] - pontoinicial['x']) * cosseno)
                    y1 = ((ponto['y'] - pontoinicial['y']) * seno)

                    x2 = ((ponto['x'] - pontoinicial['x']) * seno)
                    y2 = ((ponto['y'] - pontoinicial['y']) * cosseno)
                    
                    ponto['x'] = x1 - y1 + pontoinicial['x']
                    ponto['y'] = x2 + y2 + pontoinicial['y']


    """
    Realiza a reflexão
    Realiza a reflexão na origem, a reflexão em X e a reflexão em y
    Reflexão em relação a x deixa ele constante e troca o sinal de y
    Reflexão em relação a y deixa ele constante e troca o sinal de x
    Reflexão em relação a origem troca o sinal de x e y
    É feita a Reflexão nos objetos linhaDDA, linhaBresehan
    
    """
    def reflexao(self, rx, ry):
        for i in self.linhadda: #repete a reflexão  para todos os pontos da reta
            pontoinicial = i[0]
            for ponto in i:
                ponto['x'] = ((ponto['x'] - pontoinicial['x']) * (rx)) + pontoinicial['x']
                ponto['y'] = ((ponto['y'] - pontoinicial['y']) * (ry)) + pontoinicial['y']

        for i in self.linhabresehan:#repete a reflexão para todos os pontos da reta
            pontoinicial = i[0]
            for ponto in i:
                ponto['x'] = ((ponto['x'] - pontoinicial['x']) * (rx)) + pontoinicial['x']
                ponto['y'] = ((ponto['y'] - pontoinicial['y']) * (ry)) + pontoinicial['y']

        for i in self.circulosbresehan:
            pontoinicial = i[0]
            for ponto in i:
                ponto['x'] = ((ponto['x'] - pontoinicial['x']) * (rx)) + pontoinicial['x']
                ponto['y'] = ((ponto['y'] - pontoinicial['y']) * (ry)) + pontoinicial['y']
        self.update()

    def reflexaoX(self):
        self.reflexao(1,-1)

    def reflexaoY(self):
        self.reflexao(-1,1)

    def reflexaoOrigem(self):
        self.reflexao(-1,-1)

    def paintEvent(self, e):
        tamanho = 4
        Qcaneta = QPen(Qt.black, tamanho, Qt.SolidLine)                    
        desenhar = QPainter(self)
        desenhar.setPen(Qcaneta)    

        """
         Demonstração na tela a realização do algoritmo Cohen-Sutherland para linhas(DDA e Bresenham)
         Plota a reta para dda ou linha de bresenham com os valores arredondados 

        """


        if self.funcao == 'recortar1' and self.recortar1:
            if self.recortar1 and self.recortar2:
                Qcaneta = QPen(Qt.black, tamanho, Qt.DashLine)
                desenhar.setPen(Qcaneta)
                desenhar.drawLine(self.recortar1['x'], self.recortar1['y'], self.recortar2['x'], self.recortar1['y']) #superior
                desenhar.drawLine(self.recortar2['x'], self.recortar2['y'], self.recortar2['x'], self.recortar1['y']) #direita
                desenhar.drawLine(self.recortar1['x'], self.recortar2['y'], self.recortar2['x'], self.recortar2['y']) #inferior
                desenhar.drawLine(self.recortar1['x'], self.recortar1['y'], self.recortar1['x'], self.recortar2['y']) #esquerda

                """
                Executa o algoritimo cohen Sutherland sobre as linhas feitas em DDA
                """
                for pontoinicio, pontofim in self.linhadda:
                    valorCohenSuther = cohenSutherland(self.recortar1, self.recortar2, pontoinicio, pontofim)
                    if not valorCohenSuther:
                        continue
                    (x1, y1, x2, y2) = valorCohenSuther
                    ponto1 = {'x': x1, 'y': y1}
                    ponto2 = {'x': x2, 'y': y2}
                    for ponto in alg_bresenham(ponto1, ponto2, Qt.black):
                        desenhar.drawPoint(ponto['x'], ponto['y'])

                """
                Executa o algoritimo cohen Sutherland sobre as linhas feitas em bresehan
                """

                for pontoinicio, pontofim in self.linhabresehan:
                    valorCohenSuther = cohenSutherland(self.recortar1, self.recortar2, pontoinicio, pontofim)
                    if not valorCohenSuther:
                        continue
                    (x1, y1, x2, y2) = valorCohenSuther
                    ponto1 = {'x': x1, 'y': y1}
                    ponto2 = {'x': x2, 'y': y2}
                    for ponto in alg_bresenham(ponto1, ponto2, Qt.black):
                        desenhar.drawPoint(ponto['x'], ponto['y'])
            self.update()        

            """
            Demonstração na tela a realização do algoritimo Liang-Barsky para linhas(DDA e Bresenham)
            Plota a reta para dda ou linha de bresenham com os valores arredondados 
            """

        elif self.funcao == 'recortar2' and self.recortar1:
            if self.recortar1 and self.recortar2:
                Qcaneta = QPen(Qt.black, tamanho, Qt.DashLine)
                desenhar.setPen(Qcaneta)
                desenhar.drawLine(self.recortar1['x'], self.recortar1['y'], self.recortar2['x'], self.recortar1['y']) #superior
                desenhar.drawLine(self.recortar2['x'], self.recortar2['y'], self.recortar2['x'], self.recortar1['y']) #direita
                desenhar.drawLine(self.recortar1['x'], self.recortar2['y'], self.recortar2['x'], self.recortar2['y']) #inferior
                desenhar.drawLine(self.recortar1['x'], self.recortar1['y'], self.recortar1['x'], self.recortar2['y']) #esquerda

                for pontoinicio, pontofim in self.linhadda:
                    valorLiangBarsky = liangBarsky(self.recortar1, self.recortar2, pontoinicio, pontofim)
                    if not valorLiangBarsky:
                        continue
                    (x1, y1, x2, y2) = valorLiangBarsky
                    ponto1 = {'x': x1, 'y': y1}
                    ponto2 = {'x': x2, 'y': y2}
                    for ponto in alg_bresenham(ponto1, ponto2, Qt.black):
                        desenhar.drawPoint(ponto['x'], ponto['y'])

                for pontoinicio, pontofim in self.linhabresehan:
                    valores = liangBarsky(self.recortar1, self.recortar2, pontoinicio, pontofim)
                    if not valores:
                        continue
                    (x1, y1, x2, y2) = valores
                    ponto1 = {'x': x1, 'y': y1}
                    ponto2 = {'x': x2, 'y': y2}
                    for ponto in alg_bresenham(ponto1, ponto2, Qt.black):
                        desenhar.drawPoint(ponto['x'], ponto['y'])

            self.update()
        else:
            for ponto1,ponto2 in self.linhadda:
                for ponto in dda(ponto1,ponto2,Qt.black):
                    desenhar.drawPoint(ponto['x'],ponto['y'])
            
            for ponto1,ponto2 in self.linhabresehan:
                for ponto in alg_bresenham(ponto1,ponto2,Qt.black):
                    desenhar.drawPoint(ponto['x'],ponto['y'])

            for centro, p in self.circulosbresehan:
                for ponto in circunferenciaBresenhan(centro, p, Qt.black):
                    desenhar.drawPoint(ponto['x'],ponto['y'])

        self.update()

        """
         Limpa o canvas

        """
    def Limpar(self):
        self.circulosbresehan      = []
        self.linhabresehan    = []
        self.linhadda    = []
        self.update()  
 

"""
Criação dos sub menus que são usados quando a função Translação, Rotação ou escala é chamada, para que os valores possam ser
preenchidos e após a realização da transformação geométrica os resultados são retornado para a tela principal 
 
"""
 
"""
Criando a tela para entrada das informações que vão ser utilizadas para realizar a translação dos objetos
 
"""

class TranslacaoMenu(QDialog):
	def __init__(self, pai = None):
		super(TranslacaoMenu, self).__init__(pai)

		self.setWindowTitle('Translação')
		self.setWindowIcon(QIcon('imagens/traslacao.png'))
		menuTras = QFormLayout(self)
	
		
		# Entrada Translação Eixo X
		self.Tx = QLineEdit()
		self.Tx.setValidator(QIntValidator())
		self.Tx.setMaxLength(4)
		menuTras.addRow("Translação eixo X: ", self.Tx)

		# Entrada Translação Eixo Y
		self.Ty = QLineEdit()
		self.Ty.setValidator(QIntValidator())
		self.Ty.setMaxLength(4)
		menuTras.addRow("Translação eixo Y: ", self.Ty)

		# Butões de OK e Cancel
		butoes = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal, self)
		butoes.accepted.connect(self.accept)
		butoes.rejected.connect(self.reject)
		menuTras.addRow(butoes)

	def getX(self):
		return self.Tx.text()

	def getY(self):
		return self.Ty.text()

	# Método estático que cria e retorna (Traslação x, Traslação y, aceito)
	@staticmethod
	def getResults(pai = None):
		dialog = TranslacaoMenu(pai)
		entrada = dialog.exec_()
		Tx = dialog.getX()
		Ty = dialog.getY()
		return (Tx, -int(Ty), entrada == QDialog.Accepted)
 
"""
Criando a tela para entrada das informações que vão ser utilizadas para realizar a escala dos objetos
 
"""

class EscalaMenu(QDialog):
	def __init__(self, pai = None):
		super(EscalaMenu, self).__init__(pai)

		self.setWindowTitle('Escala')
		self.setWindowIcon(QIcon('imagens/escala.png'))
		menuEscala = QFormLayout(self)
		
		# Entrada escala valor de X 
		self.escalaSx = QDoubleSpinBox()
		self.escalaSx.setMinimum(0)
		menuEscala.addRow("Valor de Sx: ", self.escalaSx)

		# Entrada escala valor de Y
		self.escalaSy = QDoubleSpinBox()
		self.escalaSy.setMinimum(0)
		menuEscala.addRow("Valor de Sy: ", self.escalaSy)

		# Butões de OK e Cancel
		butoes = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)
		butoes.accepted.connect(self.accept)
		butoes.rejected.connect(self.reject)
		menuEscala.addRow(butoes)

	def getescalaSx(self):
		return self.escalaSx.text()

	def getescalaSy(self):
		return self.escalaSy.text()

	# Método estático  que retorna (escalaSx, escalaSy, aceito)
	@staticmethod
	def getResults(pai = None):
		dialog = EscalaMenu(pai)
		entrada = dialog.exec_()
		escalaSx = dialog.getescalaSx()
		escalaSy = dialog.getescalaSy()
		return (escalaSx, escalaSy, entrada == QDialog.Accepted)
	
"""
Criando a tela para entrada das informações que vão ser utilizadas para realizar a rotação dos objetos
 
"""

class RotacaoMenu(QDialog):
	def __init__(self, pai = None):
		super(RotacaoMenu, self).__init__(pai)
		self.setWindowTitle('Rotação')
		self.setWindowIcon(QIcon('imagens/rotacao.png'))
		menuEscala = QFormLayout(self)

		# Entrada angulo da rotação
		self.angulo = QDoubleSpinBox()
		self.angulo.setRange(-360,360)
		menuEscala.addRow("Ângulo rotação: ", self.angulo)

		# Butões de OK e Cancel
		butoes = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel,Qt.Horizontal, self)
		butoes.accepted.connect(self.accept)
		butoes.rejected.connect(self.reject)
		menuEscala.addRow(butoes)

	def getAngulo(self):
		return self.angulo.text()

	# Método estático que cria o dialog e retorna (angulo, aceito)
	@staticmethod
	def getResults(pai = None):
		dialog = RotacaoMenu(pai)
		entrada = dialog.exec_()
		angulo = dialog.getAngulo()
		angulo = float(angulo.replace(',','.'))
		angulo = angulo *-1
		return (radians(angulo), entrada == QDialog.Accepted)
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    Tela = window()
    sys.exit(app.exec_())