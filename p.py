import time
import threading
 
class th1(threading.Thread):
    def __init__(self, *args, **kwargs):
        super(th1, self).__init__(*args, **kwargs)
        self._stop = threading.Event()
    def stop(self):
        self._stop.set()
    def stopped(self):
        return self._stop.isSet()
    def run(self):
        while True:
            if self.stopped():
                return
            print("Hello, world!")
            time.sleep(1)
 
x = th1()
x.start()
time.sleep(5)
x.stop()
#x.join()