import lcm
from exlcm import example_t
import time 

msg = example_t()
msg.timestamp = 0
msg.position = (1, 2, 3)
msg.orientation = (1, 0, 0, 0)
msg.ranges = range(15)
msg.num_ranges = len(msg.ranges)
msg.name = "example string"
msg.enabled = True
lc = lcm.LCM()
print("1秒ごとにpublish")
for _ in range(5):
    lc.publish("EXAMPLE", msg.encode())
    time.sleep(1)