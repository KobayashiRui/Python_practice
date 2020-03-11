'''
最もシンプルなマルチスレッド
スレッド内でwhileが動いているためメインのスレッドが最後までいってもスレッドが動きつづけます
'''

import time
import threading

def Hoge1():
    for _ in range(10):
        print("hoge1")
        time.sleep(1)

def Hoge2():
    for _ in range(10):
        print("hoge2")
        time.sleep(1)

if __name__ == "__main__":
    #Threadコンストラクタの引数に関数を定義する
    thread1 = threading.Thread(target=Hoge1)
    thread2 = threading.Thread(target=Hoge2)

    #TODO startとrunの違い
    thread1.start()
    thread2.start()
    while True:
        a = input()
        print("input:" + a)
        if(a=="q"):
            print("break")
            break
    
    #thread1とthread2が終わるまで待機する
    thread1.join()
    thread2.join()
    print("END")
