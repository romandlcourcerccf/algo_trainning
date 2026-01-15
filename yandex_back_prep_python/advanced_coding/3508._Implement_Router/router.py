from typing import List, Any


class Router:
    def __init__(self, memory_limit):
        self._memory_limit = memory_limit

        self._packets_set = set()
        self._packets_stack = []

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        if str(source) + str(destination) + str(timestamp) in self._packets_set:
            return False

        if len(self._packets_stack) > self._memory_limit:
            packet = self._packets_stack.pop()
            self._packets_set.remove(str(packet[0]) + str(packet[1]) + str(packet[2]))

        self._packets_set.add(str(source) + str(destination) + str(timestamp))
        self._packets_stack.append([source, destination, timestamp])

        return True

    #     Remove the packet from storage.
    # Return the packet as an array [source, destination, timestamp].
    # If there are no packets to forward, return an empty array.

    def forwardPacket(self) -> List[Any]:
        if self._packets_stack:
            packet = self._packets_stack.pop()
            self._packets_set.remove(str(packet[0]) + str(packet[1]) + str(packet[2]))
            return packet

        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        res = 0

        for package in self._packets_stack:
            if package[1] == destination and startTime <= package[2] <= endTime:
                res += 1

        return res
