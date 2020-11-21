from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFrame
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QSlider
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
import numpy as np
import mundo
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure
import sys



class PanelMenu(QFrame):
    
    labelTitulo = None
    botonSimulacion = None
    botonAnalisis = None   
    actual = ""
    principal = None
    
    
    def __init__(self, pPrincipal):
        
        PanelMenu.principal = pPrincipal
        super(PanelMenu, self).__init__()
        super().setFrameShape(QFrame.StyledPanel)
        super().setStyleSheet('border-radius: 10px; background-color: #444952')
        super().setFixedHeight(100)
        PanelMenu.actual = "Simulacion"
        
        
        lay = QHBoxLayout()
        
      

        
        font = QFont()
        font.setFamily('Times font')
        font.setFixedPitch(False)
        font.setPointSize(12)
        font.setBold(True)
        
        fontTitle = QFont()
        fontTitle.setFamily('Times font')
        fontTitle.setFixedPitch(False)
        fontTitle.setPointSize(15)
        fontTitle.setBold(True)
        
        labelVacio = QLabel()
        labelVacio.setFixedWidth(30)
        lay.addWidget(labelVacio)
        
        PanelMenu.labelTitulo = QLabel()
        PanelMenu.labelTitulo.setFont(fontTitle)
        PanelMenu.labelTitulo.setText("SUPERVISOR")
        PanelMenu.labelTitulo.setStyleSheet('color: white')
        lay.addWidget(PanelMenu.labelTitulo)
        
        PanelMenu.botonSimulacion = QPushButton('SIMULACIÓN', self)
        PanelMenu.botonSimulacion.setFont(font)
        PanelMenu.botonSimulacion.setStyleSheet('background-color: #444952; color: white')
        PanelMenu.botonSimulacion.setFixedSize(200,40)
        PanelMenu.botonSimulacion.clicked.connect(self.accion1)
        PanelMenu.botonSimulacion.setEnabled(False)
        lay.addWidget(PanelMenu.botonSimulacion)
        
        PanelMenu.botonAnalisis = QPushButton('ANÁLISIS', self)
        PanelMenu.botonAnalisis.setFont(font)
        PanelMenu.botonAnalisis.setStyleSheet('background-color: #2e3138; color:gray')
        PanelMenu.botonAnalisis.setFixedSize(200,40)
        PanelMenu.botonAnalisis.clicked.connect(self.accion2)
        lay.addWidget(PanelMenu.botonAnalisis)
        
        self.setLayout(lay)
        
    
    def toggle(self):
        if PanelMenu.actual == "Analisis":
            PanelMenu.botonAnalisis.setEnabled(True)
            PanelMenu.botonAnalisis.setStyleSheet('background-color: #2e3138; color: gray')
            PanelMenu.botonSimulacion.setEnabled(False)
            PanelMenu.botonSimulacion.setStyleSheet('background-color: #444952; color: white')
          
            PanelMenu.actual = "Simulacion"
        else:
            PanelMenu.botonAnalisis.setEnabled(False)
            PanelMenu.botonAnalisis.setStyleSheet('background-color: #444952; color:white')
            PanelMenu.botonSimulacion.setEnabled(True)
            PanelMenu.botonSimulacion.setStyleSheet('background-color: #2e3138; color: gray')
            PanelMenu.actual = "Analisis"
            
    def accion1(self):
        self.toggle()
        PanelMenu.principal.toggle()
        PanelMenu.botonSimulacion.clicked.disconnect()
        PanelMenu.botonAnalisis.clicked.connect(self.accion2)
        
    def accion2(self):
        self.toggle()
        PanelMenu.principal.toggle()
        PanelMenu.botonSimulacion.clicked.connect(self.accion1)
        PanelMenu.botonAnalisis.clicked.disconnect()
        
        
        
    
        
class PanelParametros(QFrame):
    
    padre = None
    
    slider = None
    labelSlider = None
    labelValorSlider = None
    vboxLayout = None
    labelVacio = None
    panelSwitch = None
    
    swon1 = None
    swoff2 = None
    labelSwitch1 = None
    
    swon2 = None
    swoff2 = None
    labelSwitch2 = None
    
    swon3 = None
    swoff3 = None
    swSinc3 = None
    labelSwitch3 = None

    lay1 = None
    actual1 = "ON"
    actual2 = "ON"
    actual3 = "ON"
    
    botonSimular = None
    
    def __init__(self, pPadre):
        
        self.padre = pPadre
        super(PanelParametros, self).__init__()
        font = QFont()
        font.setFamily('Times font')
        font.setFixedPitch(False)
        font.setPointSize(12)
        font.setBold(True)

        PanelParametros.vboxLayout = QVBoxLayout()        
        self.setLayout(self.vboxLayout)
        
        
        PanelParametros.labelVacio = QLabel()
        
        self.labelValorSlider = QLabel('0', self)
        self.labelValorSlider.setFont(font)
        self.labelValorSlider.setFixedWidth(70)
        self.labelValorSlider.setFixedHeight(30)
        self.labelValorSlider.setStyleSheet('color:white; background-color: #444952; border-radius: 10px')
        self.labelValorSlider.setAlignment(Qt.AlignCenter);
        self.vboxLayout.addWidget(self.labelValorSlider)
        
        PanelParametros.slider = QSlider(Qt.Horizontal, self)
        PanelParametros.slider.setFixedWidth(520)
        PanelParametros.slider.setFixedHeight(30)
        PanelParametros.slider.setMinimum(1)
        PanelParametros.slider.setMaximum(1000)
        PanelParametros.slider.valueChanged[int].connect(self.changeValue)
        PanelParametros.slider.setStyleSheet('QSlider::handle:horizontal {background-color: #8ab71b;}')
        PanelParametros.vboxLayout.addWidget(PanelParametros.slider)
        
        PanelParametros.labelSlider = QLabel('RADIACIÓN')
        PanelParametros.labelSlider.setStyleSheet('color: white')
        PanelParametros.labelSlider.setFont(font)
        PanelParametros.vboxLayout.addWidget(PanelParametros.labelSlider)
        
        lbl = QLabel()
        lbl.setFixedHeight(100)
        self.vboxLayout.addWidget(lbl)

        
        self.panelSwitch = QFrame()
        self.panelSwitch.setFixedHeight(500)
        self.lay1 = QGridLayout()
        self.panelSwitch.setLayout(self.lay1)
        
        self.labelSwitch1 = QLabel('SWITCH 1')
        self.labelSwitch1.setFont(font)
        self.labelSwitch1.setStyleSheet('color: white')
        self.labelSwitch1.setAlignment(Qt.AlignCenter);
        self.labelSwitch1.setFixedWidth(200)
        self.lay1.addWidget(self.labelSwitch1,1,1)
        
        self.swon1 = QPushButton('ON', self)
        self.swon1.setFont(font)
        self.swon1.setStyleSheet('background-color: #23252a; color: white; border-radius: 10px')
        self.swon1.setFixedSize(100,40)
        self.swon1.setEnabled(False)
        self.swon1.clicked.connect(self.toggle1)
        self.lay1.addWidget(self.swon1,1,2)
        
        self.swoff1 = QPushButton('OFF', self)
        self.swoff1.setFont(font)
        self.swoff1.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
        self.swoff1.setFixedSize(100,40)
        self.swoff1.clicked.connect(self.toggle1)
        self.lay1.addWidget(self.swoff1,1,3)
        
        self.labelSwitch2 = QLabel('SWITCH 2')
        self.labelSwitch2.setFont(font)
        self.labelSwitch2.setStyleSheet('color: white')
        self.labelSwitch2.setAlignment(Qt.AlignCenter);
        self.labelSwitch2.setFixedWidth(200)
        self.lay1.addWidget(self.labelSwitch2,2,1)
        
        self.swon2 = QPushButton('ON', self)
        self.swon2.setFont(font)
        self.swon2.setStyleSheet('background-color: #23252a; color: white; border-radius: 10px')
        self.swon2.setFixedSize(100,40)
        self.swon2.setEnabled(False)
        self.swon2.clicked.connect(self.toggle2)
        self.lay1.addWidget(self.swon2,2,2)
        
        self.swoff2 = QPushButton('OFF', self)
        self.swoff2.setFont(font)
        self.swoff2.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
        self.swoff2.setFixedSize(100,40)
        self.swoff2.clicked.connect(self.toggle2)
        self.lay1.addWidget(self.swoff2,2,3)
        
        self.labelSwitch3 = QLabel('SWITCH 3')
        self.labelSwitch3.setFont(font)
        self.labelSwitch3.setStyleSheet('color: white')
        self.labelSwitch3.setAlignment(Qt.AlignCenter);
        self.labelSwitch3.setFixedWidth(200)
        self.lay1.addWidget(self.labelSwitch3,3,1)
        
        self.swon3 = QPushButton('ON', self)
        self.swon3.setFont(font)
        self.swon3.setStyleSheet('background-color: #23252a; color: white; border-radius: 10px')
        self.swon3.setFixedSize(100,40)
        self.swon3.setEnabled(False)
        self.swon3.clicked.connect(lambda: self.toggle3("ON"))
        self.lay1.addWidget(self.swon3,3,2)
        
        self.swSinc3 = QPushButton('CARGAR', self)
        self.swSinc3.setFont(font)
        self.swSinc3.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
        self.swSinc3.setFixedSize(100,40)
        self.swSinc3.clicked.connect(lambda: self.toggle3("SINC"))
        self.lay1.addWidget(self.swSinc3,3,3)
        
        self.swoff3 = QPushButton('OFF', self)
        self.swoff3.setFont(font)
        self.swoff3.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
        self.swoff3.setFixedSize(100,40)
        self.swoff3.clicked.connect(lambda: self.toggle3("OFF"))
        self.lay1.addWidget(self.swoff3,3,4)
        

        self.botonSimular = QPushButton('SIMULAR', self)
        self.botonSimular.setFont(font)
        self.botonSimular.setStyleSheet('background-color: #2aa1d3; color: white; border-radius: 10px')
        self.botonSimular.setGeometry(0,0,150, 60)
        self.botonSimular.setFixedHeight(50)
        self.botonSimular.clicked.connect(self.simular)
        
        
        
        
        self.panelSwitch.setFixedHeight(300)
        self.vboxLayout.addWidget(self.panelSwitch)
        
        self.labelVacio.setFixedHeight(100)
        
        self.vboxLayout.addWidget(self.labelVacio)
        self.vboxLayout.addWidget(self.botonSimular)

        
    def changeValue(self, value):
        valor = str(value)
        self.labelValorSlider.setText(valor)
        
    def toggle1(self):
        if(self.actual1 == "ON"):
            self.actual1 = "OFF"
            self.swon1.setEnabled(True)
            self.swon1.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
            self.swoff1.setEnabled(False)
            self.swoff1.setStyleSheet('background-color: #23252a; color: white; border-radius: 10px')
        else:
            self.actual1 = "ON"
            self.swon1.setEnabled(False)
            self.swon1.setStyleSheet('background-color: #23252a; color: white; border-radius: 10px')
            self.swoff1.setEnabled(True)
            self.swoff1.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
            
    def toggle2(self):
        if(self.actual2 == "ON"):
            self.actual2 = "OFF"
            self.swon2.setEnabled(True)
            self.swon2.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
            self.swoff2.setEnabled(False)
            self.swoff2.setStyleSheet('background-color: #23252a; color: white; border-radius: 10px')
        else:
            self.actual2 = "ON"
            self.swon2.setEnabled(False)
            self.swon2.setStyleSheet('background-color: #23252a; color: white; border-radius: 10px')
            self.swoff2.setEnabled(True)
            self.swoff2.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
            
    def toggle3(self,txt):
        if(txt == "ON"):
            self.swon3.setEnabled(False)
            self.swon3.setStyleSheet('background-color: #23252a; color: white; border-radius: 10px')
            self.swoff3.setEnabled(True)
            self.swoff3.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
            self.swSinc3.setEnabled(True)
            self.swSinc3.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
        elif (txt == "OFF"):
            self.swoff3.setEnabled(False)
            self.swoff3.setStyleSheet('background-color: #23252a; color: white; border-radius: 10px')
            self.swon3.setEnabled(True)
            self.swon3.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
            self.swSinc3.setEnabled(True)
            self.swSinc3.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
        else:
            self.swSinc3.setEnabled(False)
            self.swSinc3.setStyleSheet('background-color: #23252a; color: white; border-radius: 10px')
            self.swoff3.setEnabled(True)
            self.swoff3.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
            self.swon3.setEnabled(True)
            self.swon3.setStyleSheet('background-color: #444952; color: white; border-radius: 10px')
            
    def simular(self):

        irr = self.slider.value()
        if self.swSinc3.isEnabled():
            sinc = 0
        else:
            sinc = 1
            
        if self.swon3.isEnabled():
            on3 = 0
        else:
            on3 = 1
            
        if self.swon2.isEnabled():
            on2 = 0
        else:
            on2 = 1
            
        if self.swon1.isEnabled():
            on1 = 0
        else:
            on1 = 1
            
       
        self.padre.simular(irr, sinc, on3, on2, on1)
        self.padre.plot()
   

class PanelCuerpo(QFrame):
    actual = ""
    panelSimulacion = None
    hboxPanelCuerpo = None
    panelAnalisis = None
    padre = None
    
    def __init__(self,pPadre):
        super(PanelCuerpo, self).__init__() 
        self.padre = pPadre
        PanelCuerpo.actual = "Simulacion"
        PanelCuerpo.panelSimulacion = PanelSimulacion(self)
        PanelCuerpo.hboxPanelCuerpo = QHBoxLayout()
        PanelCuerpo.hboxPanelCuerpo.addWidget(PanelCuerpo.panelSimulacion)
        PanelCuerpo.panelAnalisis = PanelAnalisis()
        super().setLayout(PanelCuerpo.hboxPanelCuerpo)
        
    def toggle(self):
        if PanelCuerpo.actual == "Simulacion":
            PanelCuerpo.actual = "Analisis"
            PanelCuerpo.panelSimulacion.setParent(None)
            PanelCuerpo.hboxPanelCuerpo.addWidget(PanelCuerpo.panelAnalisis)
        else:
            PanelCuerpo.actual = "Simulacion"
            PanelCuerpo.panelAnalisis.setParent(None)
            PanelCuerpo.hboxPanelCuerpo.addWidget(PanelCuerpo.panelSimulacion)
        
    def plot(self):       
        self.panelSimulacion.plot()
    
    def simular(self,irr, sinc, on3, on2, on1):
        self.padre.simular(irr, sinc, on3, on2, on1)  

    def getData(self):
        return self.padre.getData()        
        
class PanelPlot(QFrame):
    flag = 0
    padre = None
    

    def __init__(self, pPadre):
        super(PanelPlot, self).__init__()
        super().setFrameShape(QFrame.StyledPanel)
        super().setStyleSheet('background-color: #444952; border-radius: 10px')
        super().setFixedWidth(1150)
        self.lay = QVBoxLayout()
        self.lay2 = QVBoxLayout()
        self.lay3 = QHBoxLayout()
        
        self.panelGrafica = QFrame( )
        self.panelBotones = QFrame( )
        
        self.panelGrafica.setStyleSheet('border-radius: 10px')
        self.panelBotones.setStyleSheet('border-radius: 10px')
        
        
        self.setLayout(self.lay)
        self.panelGrafica.setLayout(self.lay2)
        self.padre = pPadre
        self.combo = QComboBox( self )
        self.combo.addItem("VOLTAJE CARGA")
        self.combo.addItem("SOC BATERÍA")
        self.lay.addWidget(self.panelGrafica)
        
        self.panelBotones.setLayout(self.lay3)
        

        
       
        
        self.panelBotones.setFixedHeight(100)

        
        
        self.font = QFont()
        self.font.setFamily('Times font')
        self.font.setFixedPitch(False)
        self.font.setPointSize(10)
        self.font.setBold(True)
        
        
        self.combo.setStyleSheet('QComboBox'
                                       '{'
                                            'color:white;'
                                            'background-color: #23252a;'
                                            'border-radius: 10px'
                                        '}'
                                        
                                       'QComboBox::drop-down'
                                        '{'
                                            'width: 20px;'
                                            'border-color: #23252a;'
                                            'color: white'
                                            'background-color: #23252a;'
                                        '}'
                                        )  
        
        self.combo.setFont(self.font)
        
        self.combo.setEditable(True)
        self.ledit = self.combo.lineEdit()
        self.ledit.setAlignment(Qt.AlignCenter)
        self.ledit.setReadOnly(True)
        
        self.ledit.setStyleSheet('background-color:#23252a')  
        self.lay3.addWidget(self.combo)
        self.ledit.setFont(self.font)

        self.combo.setFixedSize(200,50)         
        
        
        self.lay.addWidget(self.panelBotones)
        self.panelGrafica.show()
        self.combo.currentIndexChanged.connect(self.on_currentIndexChanged)
        self.y2 = None
        self.y1 = None

        self.sc = MplCanvas(self, 5, 4, 100) 
        self.lay2.addWidget(self.sc)
        self.activar = False
    def on_currentIndexChanged( self ):
        self.plot()

    def setActivar(self):
        self.activar = True

        
    def plot(self):
        if self.activar == True:
            self.data = self.padre.getData()
            self.tiempo = self.data[:,0]  
            self.y1 = self.data[:,1]
            self.y2 = self.data[:,2]
            
            if(self.combo.currentText() == "VOLTAJE CARGA"):
                y = self.y1
            elif(self.combo.currentText() == "SOC BATERÍA"):
                y = self.y2
                
            self.sc.axes.clear()
            self.sc.axes.plot(self.tiempo, y, color = '#6a8922', linewidth = 1)  
            self.sc.draw()

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent, width, height, dpi ):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.fig.add_subplot(111)
        
        self.axes.set_facecolor('#23252a')
        self.fig.patch.set_facecolor('#444952')
        super(MplCanvas, self).__init__(self.fig)  
 
        
class PanelAnalisis(QFrame):
    def __init__(self):
        super(PanelAnalisis, self).__init__()

        
class PanelSimulacion(QFrame):

    panelParametros = None
    panelPlot = None
    padre = None
    
    def __init__(self, pPadre):
        super(PanelSimulacion, self).__init__()
        self.padre = pPadre
        PanelSimulacion.panelParametros = PanelParametros(self)
        PanelSimulacion.panelPlot = PanelPlot(self)
        hboxSimulacion = QHBoxLayout()
        hboxSimulacion.addWidget(PanelSimulacion.panelParametros)
        hboxSimulacion.addWidget(PanelSimulacion.panelPlot)
        super().setLayout(hboxSimulacion)
        
        
    def plot(self):
        self.panelPlot.setActivar()
        self.panelPlot.plot()
        
        
    def simular(self, irr, sinc, on3, on2, on1):
        self.padre.simular(irr, sinc, on3, on2, on1)
        
    def getData(self):
        return self.padre.getData()
        
        
        
class Interfaz(QWidget):

    #Crea aplicacion
    app = QApplication(sys.argv)
    panelMenu = None
    panelAnalisis = None
    panelPlot = None
    panelCuerpo = None
    
    supervisor = None
    
    #Constructor
    def __init__(self):       
        super(Interfaz, self).__init__()
        super().setWindowTitle('Supervisor')
        super().setGeometry(60, 15, 1800 , 900)
        super().move(60,15)
        super().setFixedSize(super().size())
        super().setStyleSheet('background-color: #2e3138')
        vboxPrincipal = QVBoxLayout()
        
        #Crea un supervisor
        self.supervisor = mundo.Supervisor()
        
        #Crea Panel de Menu
        Interfaz.panelMenu = PanelMenu(self)
        vboxPrincipal.addWidget(Interfaz.panelMenu)
        
        #Crea Panel de Cuerpo
        Interfaz.panelCuerpo = PanelCuerpo(self)
        vboxPrincipal.addWidget(Interfaz.panelCuerpo)
        

        super().setLayout(vboxPrincipal)     
        super().show()
        sys.exit(Interfaz.app.exec())
        
    def getData(self):
        self.scopes = self.supervisor.getData()
        return self.scopes
    
    def simular(self, irr, sinc, on3, on2, on1):
        self.supervisor.simular(irr, sinc, on3, on2, on1)
        
   
    
    #Cambia entre pestañas
    def toggle(self):
        Interfaz.panelCuerpo.toggle()
    
    
#Correr
    
Interfaz()

    
