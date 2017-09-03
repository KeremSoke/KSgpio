import sys
import webbrowser
from PyQt4.QtCore import *
from PyQt4.QtGui import *
def window():
    def About():
        msg = QMessageBox()
        msg.setText("KSgpio 1.0")
        msg.setWindowIcon(QIcon("led-icon.png"))
        msg.setIconPixmap(QPixmap("led-icon.png"))
        msg.setInformativeText("KSgpio is simple GPIO Manager")
        msg.setWindowTitle("About KSgpio")
        msg.setDetailedText("""License: GPL 2.0
Author: KS
About: KSgpio is Python, 
PyQt and pyA20 based
gpio manager for Allwinner H3.""")
        msg.exec_()
    def Help():
        class myListWidget(QListWidget):
            def Clicked(self,item):
                select = str(item.text())
                if select=="How to use KSgpio":
                    howwin = QDialog()
                    Head = QLabel("How to use KSgpio")
                    Body = QLabel("""KSgpio is an easy gpio manager developed 
for Allwinner H3 processors. To set a pin's value
to 1, select a CheckButton and press the Update button. 
Press the Clear button to set the value of all 
pins to 0. Remember, each check button represents a pin.""")
                    vbox = QVBoxLayout()
                    vbox.addWidget(Head)
                    vbox.addStretch()
                    vbox.addWidget(Body)
                    howwin.setLayout(vbox)
                    howwin.setWindowTitle("Help documention")
                    howwin.setWindowIcon(QIcon("documention-icon.png"))
                    howwin.show()
                    howwin.exec_()
                if select=="Shortcut help":
                    howwin = QDialog()
                    Head = QLabel("Shortcut help")
                    Body = QLabel("""ALT + U --> UPDATE
ALT + C --> CLEAR
ALT + A --> ABOUT
ALT + H --> HELP""")
                    vbox = QVBoxLayout()
                    vbox.addWidget(Head)
                    vbox.addStretch()
                    vbox.addWidget(Body)
                    howwin.setLayout(vbox)
                    howwin.setWindowTitle("Help documention")
                    howwin.setWindowIcon(QIcon("documention-icon.png"))
                    howwin.show()
                    howwin.exec_()
                if select=="Examples":
                    howwin = QDialog()
                    Head = QLabel("Examples")
                    Imgl = QLabel("Schematic")
                    Image = QLabel()
                    Image.setPixmap(QPixmap("example_h3.png"))
                    body = QLabel("""Make the above circuit and select "PA12" 
check button from KSgpio and press 
"Update" button.""")
                    vbox = QVBoxLayout()
                    vbox.addWidget(Head)
                    vbox.addStretch()
                    vbox.addWidget(Imgl)
                    vbox.addWidget(Image)
                    vbox.addStretch()
                    vbox.addWidget(body)
                    howwin.setLayout(vbox)
                    howwin.setWindowTitle("Help documention")
                    howwin.setWindowIcon(QIcon("documention-icon.png"))
                    howwin.show()
                    howwin.exec_()
                if select=="Allwinner H3 Pinout(OPi)":
                    howwin = QDialog()
                    Head = QLabel("Allwinner H3 Pinout(OPi)")
                    Body = QLabel()
                    Body.setPixmap(QPixmap("H3_PINOUT.png"))
                    vbox = QVBoxLayout()
                    vbox.addWidget(Head)
                    vbox.addStretch()
                    vbox.addWidget(Body)
                    howwin.setLayout(vbox)
                    howwin.setWindowTitle("Help documention")
                    howwin.setWindowIcon(QIcon("documention-icon.png"))
                    howwin.show()
                    howwin.exec_()
                if select=="pyA20 downloads":
                    def clicked():
                        webbrowser.open_new("https://pypi.python.org/pypi/pyA20")
                    def clicked1():
                        webbrowser.open_new("https://github.com/duxingkei33/orangepi_PC_gpio_pyH3")
                    howwin = QDialog()
                    Head = QLabel("pyA20 0.2.1")
                    Body = QLabel("""
Control GPIO, I2C and SPI
This package provide methods for controlling GPIO pins, I2C and SPI buses.
-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-
Downloads:
pip install pya20""")
                    GotoPypib = QLabel()
                    GotoPypib.setText("<A href='https://pypi.python.org/pypi/pyA20'>Go to pyA20 Python page</a>")
                    GotoPypib.linkActivated.connect(clicked)
                    GotoGithub = QLabel("<A href='https://github.com/duxingkei33/orangepi_PC_gpio_pyH3'>Go to pyA20 GitHub page</a>")
                    GotoGithub.linkActivated.connect(clicked1)
                    vbox = QVBoxLayout()
                    vbox.addWidget(Head)
                    vbox.addStretch()
                    vbox.addWidget(Body)
                    vbox.addWidget(GotoPypib)
                    vbox.addWidget(GotoGithub)
                    howwin.setLayout(vbox)
                    howwin.setWindowTitle("Help documention")
                    howwin.setWindowIcon(QIcon("documention-icon.png"))
                    howwin.show()
                    howwin.exec_()
        listwidget = myListWidget()
        listwidget.addItem("How to use KSgpio")
        listwidget.addItem("Shortcut help")
        listwidget.addItem("Examples")
        listwidget.addItem("Allwinner H3 Pinout(OPi)")
        listwidget.addItem("pyA20 downloads")
        listwidget.setWindowTitle("Select a help documention")
        listwidget.setWindowIcon(QIcon("documention-icon.png"))
        listwidget.itemClicked.connect(listwidget.Clicked)
        listwidget.show()
        listwidget.exec_()
    def Clear():
        v331.setChecked(False)
        v51.setChecked(False)
        PA12.setChecked(False)
        v52.setChecked(False)
        PA11.setChecked(False)
        Gnd1.setChecked(False)
        PA6.setChecked(False)
        PA13.setChecked(False)
        Gnd2.setChecked(False)
        PA14.setChecked(False)
        PA1.setChecked(False)
        PD14.setChecked(False)
        PA0.setChecked(False)
        Gnd3.setChecked(False)
        PA3.setChecked(False)
        PC4.setChecked(False)
        v332.setChecked(False)
        PC7.setChecked(False)
        PC0.setChecked(False)
        Gnd4.setChecked(False)
        PC1.setChecked(False)
        PA2.setChecked(False)
        PC2.setChecked(False)
        PC3.setChecked(False)
        Gnd5.setChecked(False)
        PA21.setChecked(False)
        PA19.setChecked(False)
        PA18.setChecked(False)
        PA7.setChecked(False)
        Gnd6.setChecked(False)
        PA8.setChecked(False)
        PG8.setChecked(False)
        PA9.setChecked(False)
        Gnd7.setChecked(False)
        PA10.setChecked(False)
        PG9.setChecked(False)
        PA20.setChecked(False)
        PG6.setChecked(False)
        Gnd8.setChecked(False)
        PG7.setChecked(False)
    def Update():
        try:
            from pyA20.gpio import gpio
            from pyA20.gpio import port
        except ImportError:
            msg = QMessageBox()
            msg.setText("pyA20 module not found.")
            msg.setWindowIcon(QIcon("error.png"))
            msg.setIconPixmap(QPixmap("error.png"))
            msg.setInformativeText("For download pyA20 module Help>pyA20 downloads")
            msg.setWindowTitle("Import Error")
            msg.setDetailedText("""pyA20 module not found. For install pyA20
module go to Help>pyA20 downloads.
Error Number: 061wp64""")
            msg.exec_()
        try:
            gpio.init()
        except:
            msg = QMessageBox()
            msg.setText("pyA20 module failed to initialize")
            msg.setWindowIcon(QIcon("error.png"))
            msg.setIconPixmap(QPixmap("error.png"))
            msg.setInformativeText("pyA20 module failed to initialize")
            msg.setWindowTitle("Initialize Error")
            msg.setDetailedText("""pyA20 module failed to initialize.
Error Number: 061wp40""")
        try:
            gpio.setcfg(port.PA12, gpio.OUTPUT)
            gpio.setcfg(port.PA11, gpio.OUTPUT)
            gpio.setcfg(port.PA6, gpio.OUTPUT)
            gpio.setcfg(port.PA13, gpio.OUTPUT)
            gpio.setcfg(port.PA14, gpio.OUTPUT)
            gpio.setcfg(port.PA1, gpio.OUTPUT)
            gpio.setcfg(port.PD14, gpio.OUTPUT)
            gpio.setcfg(port.PA0, gpio.OUTPUT)
            gpio.setcfg(port.PA3, gpio.OUTPUT)
            gpio.setcfg(port.PC4, gpio.OUTPUT)
            gpio.setcfg(port.PC7, gpio.OUTPUT)
            gpio.setcfg(port.PC0, gpio.OUTPUT)
            gpio.setcfg(port.PA0, gpio.OUTPUT)
            gpio.setcfg(port.PA3, gpio.OUTPUT)
            gpio.setcfg(port.PC4, gpio.OUTPUT)
            gpio.setcfg(port.PC7, gpio.OUTPUT)
            gpio.setcfg(port.PC0, gpio.OUTPUT)
            gpio.setcfg(port.PC1, gpio.OUTPUT)
            gpio.setcfg(port.PA2, gpio.OUTPUT)
            gpio.setcfg(port.PC2, gpio.OUTPUT)
            gpio.setcfg(port.PC3, gpio.OUTPUT)
            gpio.setcfg(port.PA21, gpio.OUTPUT)
            gpio.setcfg(port.PA19, gpio.OUTPUT)
            gpio.setcfg(port.PA18, gpio.OUTPUT)
            gpio.setcfg(port.PA7, gpio.OUTPUT)
            gpio.setcfg(port.PA8, gpio.OUTPUT)
            gpio.setcfg(port.PG8, gpio.OUTPUT)
            gpio.setcfg(port.PA9, gpio.OUTPUT)
            gpio.setcfg(port.PA10, gpio.OUTPUT)
            gpio.setcfg(port.PG9, gpio.OUTPUT)
            gpio.setcfg(port.PA20, gpio.OUTPUT)
            gpio.setcfg(port.PG6, gpio.OUTPUT)
            gpio.setcfg(port.PG7, gpio.OUTPUT)
        except:
            msg = QMessageBox()
            msg.setText("pyA20 module configuration error")
            msg.setWindowIcon(QIcon("error.png"))
            msg.setIconPixmap(QPixmap("error.png"))
            msg.setInformativeText("Error in input/output configuration ")
            msg.setWindowTitle("Config Error")
            msg.setDetailedText("""Error in input/output configuration
Error Number: 061wp093""")
        if PA12.isChecked()==1:
            gpio.output(port.PA12, 1)
        else:
            gpio.output(port.PA12, 0)
        if PA11.isChecked()==1:
            gpio.output(port.PA11, 1)
        else:
            gpio.output(port.PA11, 0)
        if PA6.isChecked()==1:
            gpio.output(port.PA6, 1)
        else:
            gpio.output(port.PA6, 0)
        if PA13.isChecked()==1:
            gpio.output(port.PA13, 1)
        else:
            gpio.output(port.PA13, 0)
        if PA14.isChecked()==1:
            gpio.output(port.PA14, 1)
        else:
            gpio.output(port.PA14, 0)
        if PA1.isChecked()==1:
            gpio.output(port.PA1, 1)
        else:
            gpio.output(port.PA1, 0)
        if PD14.isChecked()==1:
            gpio.output(port.PD14, 1)
        else:
            gpio.output(port.PD14, 0)
        if PA0.isChecked()==1:
            gpio.output(port.PA0, 1)
        else:
            gpio.output(port.PA0, 0)
        if PA3.isChecked()==1:
            gpio.output(port.PA3, 1)
        else:
            gpio.output(port.PA3, 0)
        if PC4.isChecked()==1:
            gpio.output(port.PC4, 1)
        else:
            gpio.output(port.PC4, 0)
        if PC7.isChecked()==1:
            gpio.output(port.PC7, 1)
        else:
            gpio.output(port.PA7, 0)
        if PC0.isChecked()==1:
            gpio.output(port.PC0, 1)
        else:
            gpio.output(port.PC0, 0)
        if PC1.isChecked()==1:
            gpio.output(port.PC1, 1)
        else:
            gpio.output(port.PC1, 0)
        if PA2.isChecked()==1:
            gpio.output(port.PA2, 1)
        else:
            gpio.output(port.PA2, 0)
        if PC2.isChecked()==1:
            gpio.output(port.PC2, 1)
        else:
            gpio.output(port.PC2, 0)
        if PC3.isChecked()==1:
            gpio.output(port.PC3, 1)
        else:
            gpio.output(port.PC3, 0)
        if PA21.isChecked()==1:
            gpio.output(port.PA21, 1)
        else:
            gpio.output(port.PA21, 0)
        if PA19.isChecked()==1:
            gpio.output(port.PA19, 1)
        else:
            gpio.output(port.PA19, 0)
        if PA18.isChecked()==1:
            gpio.output(port.PA18, 1)
        else:
            gpio.output(port.PA18, 0)
        if PA7.isChecked()==1:
            gpio.output(port.PA7, 1)
        else:
            gpio.output(port.PA7, 0)
        if PA8.isChecked()==1:
            gpio.output(port.PA8, 1)
        else:
            gpio.output(port.PA8, 0)
        if PG8.isChecked()==1:
            gpio.output(port.PG8, 1)
        else:
            gpio.output(port.PG8, 0)
        if PA9.isChecked()==1:
            gpio.output(port.PA9, 1)
        else:
            gpio.output(port.PA9, 0)
        if PA10.isChecked()==1:
            gpio.output(port.PA10, 1)
        else:
            gpio.output(port.PA10, 0)
        if PG9.isChecked()==1:
            gpio.output(port.PG9, 1)
        else:
            gpio.output(port.PG9, 0)
        if PA20.isChecked()==1:
            gpio.output(port.PA20, 1)
        else:
            gpio.output(port.PA20, 0)
        if PG6.isChecked()==1:
            gpio.output(port.PG6, 1)
        else:
            gpio.output(port.PG6, 0)
        if PG7.isChecked()==1:
            gpio.output(port.PG7, 1)
        else:
            gpio.output(port.PG7, 0)
    app = QApplication(sys.argv)
    win = QWidget()
    grid = QGridLayout()
    first = QLabel("First 20")
    last = QLabel("Last 20")
    block = QLabel("|")
    block1 = QLabel("|")
    block2= QLabel("|")
    block3 = QLabel("|")
    block4 = QLabel("|")
    block5 = QLabel("|")
    block6 = QLabel("|")
    block7 = QLabel("|")
    block8 = QLabel("|")
    block9 = QLabel("|")
    block10 = QLabel("|")
    block11 = QLabel("|")
    v331 = QCheckBox("3.3v")
    v51 = QCheckBox("5v")
    PA12 = QCheckBox("PA12")
    v52 = QCheckBox("5v")
    PA11 = QCheckBox("PA11")
    Gnd1 = QCheckBox("GND")
    PA6 = QCheckBox("PA6")
    PA13 = QCheckBox("PA13")
    Gnd2 = QCheckBox("GND")
    PA14 = QCheckBox("PA14")
    PA1 = QCheckBox("PA1")
    PD14 = QCheckBox("PD14")
    PA0 = QCheckBox("PA0")
    Gnd3 = QCheckBox("GND")
    PA3 = QCheckBox("PA3")
    PC4 = QCheckBox("PC4")
    v332 = QCheckBox("3.3v")
    PC7 = QCheckBox("PC7")
    PC0 = QCheckBox("PC0")
    Gnd4 = QCheckBox("GND")
    PC1 = QCheckBox("PC1")
    PA2 = QCheckBox("PA2")
    PC2 = QCheckBox("PC2")
    PC3 = QCheckBox("PC3")
    Gnd5 = QCheckBox("GND")
    PA21 = QCheckBox("PA21")
    PA19 = QCheckBox("PA19")
    PA18 = QCheckBox("PA18")
    PA7 = QCheckBox("PA7")
    Gnd6 = QCheckBox("GND")
    PA8 = QCheckBox("PA8")
    PG8 = QCheckBox("PG8")
    PA9 = QCheckBox("PA9")
    Gnd7 = QCheckBox("GND")
    PA10 = QCheckBox("PA10")
    PG9 = QCheckBox("PG9")
    PA20 = QCheckBox("PA20")
    PG6 = QCheckBox("PG6")
    Gnd8 = QCheckBox("GND")
    PG7 = QCheckBox("PG7")
    Updateb = QPushButton("&Update")
    Clearb = QPushButton("&Deselect all")
    Aboutb = QPushButton("&About")
    Helpb = QPushButton("&Help")
    grid.addWidget(first,0,1)
    grid.addWidget(v331,1,1)
    grid.addWidget(v51, 1, 2)
    grid.addWidget(PA12, 2, 1)
    grid.addWidget(v52, 2, 2)
    grid.addWidget(PA11, 3, 1)
    grid.addWidget(Gnd1, 3, 2)
    grid.addWidget(PA6, 4, 1)
    grid.addWidget(PA13, 4, 2)
    grid.addWidget(Gnd2, 5, 1)
    grid.addWidget(PA14, 5, 2)
    grid.addWidget(PA1, 6, 1)
    grid.addWidget(PD14, 6, 2)
    grid.addWidget(PA0, 7, 1)
    grid.addWidget(Gnd3, 7, 2)
    grid.addWidget(PA3, 8, 1)
    grid.addWidget(PC4, 8, 2)
    grid.addWidget(v332, 9, 1)
    grid.addWidget(PC7, 9, 2)
    grid.addWidget(PC0, 10, 1)
    grid.addWidget(Gnd4, 10, 2)
    grid.addWidget(block,0,3)
    grid.addWidget(block1, 1, 3)
    grid.addWidget(block2, 2, 3)
    grid.addWidget(block3, 3, 3)
    grid.addWidget(block4, 4, 3)
    grid.addWidget(block5, 5, 3)
    grid.addWidget(block6, 6, 3)
    grid.addWidget(block7, 7, 3)
    grid.addWidget(block8, 8, 3)
    grid.addWidget(block9, 9, 3)
    grid.addWidget(block10, 10, 3)
    grid.addWidget(block11, 11,3)
    grid.addWidget(last,0,4)
    grid.addWidget(PC1, 1, 4)
    grid.addWidget(PA2, 1, 5)
    grid.addWidget(PC2, 2, 4)
    grid.addWidget(PC3, 2, 5)
    grid.addWidget(Gnd5, 3, 4)
    grid.addWidget(PA21, 3, 5)
    grid.addWidget(PA19, 4, 4)
    grid.addWidget(PA18, 4, 5)
    grid.addWidget(PA7, 5, 4)
    grid.addWidget(Gnd6, 5, 5)
    grid.addWidget(PA8, 6, 4)
    grid.addWidget(PG8, 6, 5)
    grid.addWidget(PA9, 7, 4)
    grid.addWidget(Gnd7, 7, 5)
    grid.addWidget(PA10, 8, 4)
    grid.addWidget(PG9, 8, 5)
    grid.addWidget(PA20, 9, 4)
    grid.addWidget(PG6, 9, 5)
    grid.addWidget(Gnd8, 10, 4)
    grid.addWidget(PG7, 10, 5)
    grid.addWidget(Updateb, 11, 1)
    grid.addWidget(Clearb, 11, 2)
    grid.addWidget(Aboutb,11,4)
    grid.addWidget(Helpb,11,5)
    Aboutb.clicked.connect(About)
    Helpb.clicked.connect(Help)
    Clearb.clicked.connect(Clear)
    Updateb.clicked.connect(Update)
    win.setLayout(grid)
    win.setWindowTitle("KSgpio")
    win.setWindowIcon(QIcon("led-icon.png"))
    win.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    window()
