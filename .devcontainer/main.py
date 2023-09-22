import sys
import form
from PyQt5.QtCore import QStandardPaths, QDir
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget


class Window(QMainWindow, form.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.center()
        dirNaam = QStandardPaths.locate(QStandardPaths.GenericDataLocation, str(), QStandardPaths.LocateDirectory)
        saveDir = dirNaam + "QtDesigner/"
        myDir = QDir()
        if not myDir.exists(saveDir):
            myDir.mkpath(saveDir)

    def errors(self, title, content):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(content)
        msg.exec()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def closeApp(self):
        exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())
