'''
Use library PYQT5 from module qtpy to make a user interface for the web scrapping program
'''
import sys
import PyQt5.QtWidgets as pyqt5

sys.path.insert(0, "./D2-web-scrapping/lib/python3.10/site-packages")



def dialog():
    mbox = pyqt5.QMessageBox()
    mbox.setText("Your allegiance has been noted")
    mbox.setDetailedText("You are now a disciple and subject of the all-knowing Guru")
    mbox.setStandardButtons(pyqt5.QMessageBox.Ok | pyqt5.QMessageBox.Cancel)
            
    mbox.exec_()

if __name__ == "__main__":
    app = pyqt5.QApplication(sys.argv)
    w = pyqt5.QWidget()
    w.resize(300,300)
    w.setWindowTitle("Guru99")
    
    label = pyqt5.QLabel(w)
    label.setText("Behold the Guru, Guru99")
    label.move(100,130)
    label.show()

    btn = pyqt5.QPushButton(w)
    btn.setText('Beheld')
    btn.move(110,150)
    btn.show()
    btn.clicked.connect(dialog)

    
    w.show()
    sys.exit(app.exec_())