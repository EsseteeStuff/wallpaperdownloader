import sys
import os
import requests
from PyQt5.QtCore import QStandardPaths, QDir
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
import form, config, choose
import urllib.request

# https://stackoverflow.com/questions/31836104/pyinstaller-and-onefile-how-to-include-an-image-in-the-exe-file

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

Logo = resource_path("Logo.png")


currentDir = QStandardPaths.locate(QStandardPaths.StandardLocation.GenericDataLocation, str(), QStandardPaths.LocateOption.LocateDirectory) + 'ScrapeWallpapers/'
myDir = QDir()
if not myDir.exists(currentDir):
    myDir.mkpath(currentDir)

wallPaperDir = QStandardPaths.locate(QStandardPaths.StandardLocation.GenericDataLocation, str(), QStandardPaths.LocateOption.LocateDirectory) + 'wallpapers/'
if not myDir.exists(wallPaperDir):
    myDir.mkpath(wallPaperDir)

opslagNaam = "page.txt"


class Window(QMainWindow, form.Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.center()
        self.init()

    def init(self):
        for item in config.baseResolution:
            self.cbxResolution.addItem(item)
        self.cbxResolution.setCurrentIndex(0)
        
        for item in config.baseCategorie:
            self.cbxCategorie.addItem(item)
        self.cbxCategorie.setCurrentIndex(0)

        categorie = self.cbxCategorie.currentText().lower()
        resolution = self.cbxResolution.currentText().lower()

        self.url = config.baseUrl + "/catalog/" + categorie + "/" + resolution
        result = requests.get(self.url)
        res = result.text
        config.savePage(res, opslagNaam)

        self.cbxCategorie.currentTextChanged.connect(self.keuze)
        self.cbxResolution.currentTextChanged.connect(self.keuze)
        self.btnStartDownload.clicked.connect(self.startDownload)

    def startDownload(self):
        self.lblGedaan.setText("")
        categorie = self.cbxCategorie.currentText().lower()
        resolution = self.cbxResolution.currentText().lower()
        self.picsToDownload = self.spinBox.value()

        self.saveDir = wallPaperDir + categorie + "/"
        if not myDir.exists(self.saveDir):
            myDir.mkpath(self.saveDir)

        self.url = config.baseUrl + "/catalog/" + categorie + "/" + resolution
        result = requests.get(self.url)
        res = result.text
        config.savePage(res, opslagNaam)
        urls = choose.getWallpapers(opslagNaam)

        pages = choose.getPages(opslagNaam)
        totalPics = pages * 15
        if self.picsToDownload > totalPics:
            self.picsToDownload = totalPics
        
        self.progressBar.setMinimum(0)
        self.progressBar.setMaximum(self.picsToDownload)

        self.pagNr = 1
        self.teller = 0
        self.firstRun(urls)
        
        while self.teller < self.picsToDownload:
            prefix = self.saveDir
            self.pagNr += 1
            urlsMore = config.baseUrl + "/catalog/" + categorie + "/" + resolution + "/page" + str(self.pagNr)
            result = requests.get(urlsMore)
            res = result.text
            config.savePage(res, opslagNaam)
            urls = choose.getWallpapers(opslagNaam)
            for links in urls:
                imageName = links.split('/')
                filename = prefix + imageName[-1]
                self.teller += 1
                self.progressBar.setValue(self.teller)
                image_url = links
                urllib.request.urlretrieve(image_url, filename)
                
                
        self.progressBar.setFormat("Done!")
        self.lblGedaan.setText("Wallpapers saved to: " + self.saveDir)
        self.init()

    def firstRun(self, urls):
        prefix = self.saveDir
        for links in urls:
            imageName = links.split('/')
            filename = prefix + imageName[-1]
            self.teller += 1
            self.progressBar.setValue(self.teller)
            image_url = links
            urllib.request.urlretrieve(image_url, filename)
            

    def keuze(self):
        categorie = self.cbxCategorie.currentText().lower()
        resolution = self.cbxResolution.currentText().lower()
        self.url = config.baseUrl + "/catalog/" + categorie + "/" + resolution


    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())


# pyinstaller.exe --name WallpaperDownloader --onefile --windowed --icon=icon.ico main.py