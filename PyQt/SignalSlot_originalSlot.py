import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.show()
        
    def init_ui(self):
        self.button1 = QPushButton('1')
        self.button2 = QPushButton('2')

        layout = QVBoxLayout(self)
        layout.addWidget(self.button1)
        layout.addWidget(self.button2)

        # シグナルにスロットを接続
        self.button1.clicked.connect(self.button_clicked)
        self.button2.clicked.connect(self.button_clicked)
        
    def button_clicked(self):
        # シグナルを発行したオブジェクトを取得
        # buttonはself.button1かself.button2になる
        button = self.sender()
        if button is self.button1:
            print('button 1')
        elif button is self.button2:
            print('button 2')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWidget()
    sys.exit(app.exec_())