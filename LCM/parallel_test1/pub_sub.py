import time
import threading
import lcm
from exlcm import example_t
def my_handler(channel, data):
    msg = example_t.decode(data)
    print("Received message on channel \"%s\"" % channel)
    print("   timestamp   = %s" % str(msg.timestamp))
    print("   position    = %s" % str(msg.position))
    print("   orientation = %s" % str(msg.orientation))
    print("   ranges: %s" % str(msg.ranges))
    print("   name        = '%s'" % msg.name)
    print("   enabled     = %s" % str(msg.enabled))
    print("")

def subscribe_handler(handle):
    while True:
        handle()

lc = lcm.LCM()
subscription = lc.subscribe("EXAMPLE", my_handler)
thread1 = threading.Thread(target=subscribe_handler, args=(lc.handle,))
thread1.start()
print("2秒ごとにhiが表示->publishされたらサブスレがうごく")
try:
    while True:
        print("hi")
        time.sleep(2)
except KeyboardInterrupt:
    pass
