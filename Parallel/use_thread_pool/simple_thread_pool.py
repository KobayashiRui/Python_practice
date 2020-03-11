import time
import concurrent.futures

def hoge():
    print("hoge")

if __name__ == "__main__":
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=1)
    executor.submit(hoge)