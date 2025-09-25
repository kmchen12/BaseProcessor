from multiprocessing import Queue
import time
import threading
from libs.base import BaseProcessor
# test_fork
class TEST(BaseProcessor):
    def __init__(self, name:str):
        super().__init__(name)

    def on_start(self):
        print(f"{self.name} on_start")
    
    def on_stop(self):
        print(f"{self.name} on_stop")
    
    def loop(self):
        data = self.input_queue.get(timeout=0.2)
        self.output_queue.put(self.name)

def print_thread(data, times):
    for i in range(times):
        print(data)
        time.sleep(0.2)

def main():
    a_queue = Queue() # 請一定要使用 multiprocessing.Queue
    b_queue = Queue()
    a = TEST('a')
    b = TEST('b')
    a.set_queue(a_queue, b_queue)
    b.set_queue(b_queue, a_queue)
    a.start()
    b.start()
    # a_queue.put('a')
    thread1 = threading.Thread(target=print_thread, args=("thread1", 20))
    thread2 = threading.Thread(target=print_thread, args=("thread2", 20))
    thread1.start()
    thread2.start()

    ###
    #這裡可以執行一些 main 的運算
    while True:
        text = input()
        if 's' in text:
            break
    ###

    # 等待 Thread 結束
    thread1.join()
    thread2.join()

    a.stop()
    b.stop()


if __name__ == "__main__":    

    main()
