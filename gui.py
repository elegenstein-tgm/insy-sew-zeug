__author__ = 'fusions'
import sys, csv
from PyQt5 import QtCore, QtGui, QtWidgets
from form import Ui_MainWindow


class MyDialog(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = QtGui.QStandardItemModel(self)
        #tablesettings and so stuf
        self.doGuiPostInit()

    def doGuiPostInit(self):
        self.ui.tableView.setModel(self.model)
        self.ui.actionImport.triggered.connect(self.opnfil)
        #self.ui.actionImport.triggered.
        #self.ui.actionImport.clicked.connect(self.opnfil())
        #self.opnfil()

    def opnfil(self):
        filename = QtWidgets.QFileDialog.getOpenFileName(None, 'Open ', '/home')[0]
        self.readAndInsertCSV(filename)

    def readAndInsertCSV(self, filename):
        with open(filename, "r") as filein:
            for row in csv.reader(filein):
                items = [
                    QtGui.QStandardItem(field)
                    for field in row
                    ]
                self.model.appendRow(items)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    myapp = MyDialog()
    myapp.show()
    sys.exit(app.exec_())

