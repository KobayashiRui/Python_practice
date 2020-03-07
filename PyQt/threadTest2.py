import sys
import time

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot, pyqtSignal

import threading


def logthread(caller):
    print('%-25s: %s, %s,' % (caller, threading.current_thread().name,
                              threading.current_thread().ident))


class MyApp(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)

        self.setGeometry(300, 300, 280, 600)
        self.setWindowTitle('using threads')

        self.layout = QtWidgets.QVBoxLayout(self)

        self.testButton = QtWidgets.QPushButton("QThread")
        self.testButton.released.connect(self.test)
        self.listwidget = QtWidgets.QListWidget(self)

        self.layout.addWidget(self.testButton)
        self.layout.addWidget(self.listwidget)

        logthread('mainwin.__init__')

    def add(self, text):
        """ Add item to list widget """
        logthread('mainwin.add')
        #ここでエラー警告が出る→スレッドにてGUIを変更しているのが原因?
        #警告内容
        #QObject::connect: Cannot queue arguments of type 'QList<QPersistentModelIndex>'
        #(Make sure 'QList<QPersistentModelIndex>' is registered using qRegisterMetaType().)

        self.listwidget.addItem(text)
        self.listwidget.sortItems()

    
    def endThread(self):
        print("END") 

    #ボタンが押されたら実行される
    def test(self):
        #スレッドの作成
        my_thread = QtCore.QThread(parent=self)

        # This causes my_worker.run() to eventually execute in my_thread:

        #GenericWorkerクラスにaddBatch関数を渡して実体化
        my_worker = GenericWorker()
        #my_workerをmy_threadスレッドに移動する
        my_worker.moveToThread(my_thread)

        #my_worker.start.emit("hello")
        #シグナルとコネクトする
        my_worker.make_item.connect(self.add)
        my_worker.finished.connect(self.endThread)
        my_worker.finished.connect()
        my_worker.run()

        # my_worker.finished.connect(self.xxx)

        #self.threadPool.append(my_thread)
        #my_worker.finished.connect(self.endThread)
        self.my_worker = my_worker
        my_thread.start()


class GenericWorker(QtCore.QObject):

    start = pyqtSignal(str)
    make_item = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(GenericWorker, self).__init__()
        logthread('GenericWorker.__init__')
        self.args = args
        self.kwargs = kwargs
        #self.start.connect(self.run)

    @pyqtSlot()
    def run(self, *args, **kwargs):
        logthread('GenericWorker.run')
        #self.function(*self.args, **self.kwargs)
        self.addBatch()
        self.finished.emit()

    def addBatch(self, text="test", iters=6, delay=0.3):
        """ Add several items to list widget """
        logthread('mainwin.addBatch')
        for i in range(iters):
            time.sleep(delay)  # artificial time delay
            #logthread('mainwin.add')
            self.make_item.emit(text+" "+str(i))
            #self.add(text+" "+str(i))


# run
app = QtWidgets.QApplication(sys.argv)
test = MyApp()
test.show()
app.exec_()