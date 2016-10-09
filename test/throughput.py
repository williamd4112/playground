# This script is used to test the throughput and frame rate of unrealcv.
import time, sys, argparse
from unrealcv import client
client.connect()

def cmd():
    # sync command
    # res = client.request('vget /unrealcv/echo hello')
    # res = client.request('vget /unrealcv/async_echo hello')
    # print res
    res = client.request('vget /camera/0/location')
    print res
    res = client.request('vget /camera/0/rotation')
    print res
    # print res

    # async command
    # res = client.request('vget /camera/0/lit')
    # res = client.request('vget /camera/0/depth depth.exr')

class FPSCounter:
    def __init__(self):
        self.start_index = 0
        self.start_time = time.time()

    def tick(self, current_index):
        current_time = time.time()
        if (current_time - self.start_time > 1):
            print '%d fps' % (current_index - self.start_index)
            self.start_index = current_index
            self.start_time = current_time

def main():
    counter = FPSCounter()
    n_iter = 1000000
    for i in range(n_iter):
        counter.tick(i)
        cmd()

    time.sleep(5)

if __name__ == '__main__':
    main()
