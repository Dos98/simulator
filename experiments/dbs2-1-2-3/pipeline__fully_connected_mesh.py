import fully_connected_mesh as simulator
import time

n0 = simulator.Node(0)
n0.start()

simulator.queues[0].put((0, -1)) # Peer, chunk, splitter
simulator.queues[0].put((1, -1))

n1 = simulator.Node(1)
n1.start()

simulator.queues[0].put((2, -1))
simulator.queues[0].put((3, -1))

n2 = simulator.Node(2)
n2.start()

for i in range(30):
    simulator.queues[0].put((i+4, -1))


