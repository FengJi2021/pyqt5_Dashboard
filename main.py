import sys
from ui_interface import *
from Custom_Widgets.Widgets import * #install GTK+

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
        
        loadJsonStyle(self, self.ui)
        
        # expand center menu 
        self.ui.settingBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.centerMenuContainer.expandMenu())
        
        # collapse center menu
        self.ui.closeCenterMenu.clicked.connect(lambda: self.ui.centerMenuContainer.collapseMenu())
        
        # expand right container and collapse it
        self.ui.rightContainerBtn.clicked.connect(lambda: self.ui.rightMenuContainer.expandMenu())
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.rightMenuContainer.collapseMenu())
        
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())