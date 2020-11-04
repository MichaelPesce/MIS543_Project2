import random

from .BasicTest import *
from time import sleep

"""
This tests random packet drops. We randomly decide to drop about half of the
packets that go through the forwarder in either direction.

Note that to implement this we just needed to override the handle_packet()
method -- this gives you an example of how to extend the basic test case to
create your own.
"""
class RandomDelayTest(BasicTest):
    def handle_packet(self):
        for p in self.forwarder.in_queue:
            choice = random.choice([True, False])
            if choice:
                sleep(1)
            self.forwarder.out_queue.append(p)
        print(self.forwarder.out_queue)
        # empty out the in_queue
        self.forwarder.in_queue = []
