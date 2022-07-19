"""
You have a RecentCounter class which counts the number of recent requests within a certain time frame.

Implement the RecentCounter class:

RecentCounter() Initializes the counter with zero recent requests.
int ping(int t) Adds a new request at time t, where t represents some time in milliseconds
and returns the number of requests that has happened in the past 3000 milliseconds (including the new request).
Specifically, return the number of requests that have happened in the inclusive range [t - 3000, t].
It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.


"""


class RecentCounter:

    def __init__(self):
        self.counter = []

    def ping(self, t: int) -> int:
        self.counter.append(t)
        res = 0
        i = len(self.counter) - 1
        print(i)
        while i >= 0 and self.counter[i] >= t - 3000:
            res += 1
            i -= 1
        return res

    def ping1(self, t: int) -> int:
        self.counter.append(t)
        while self.counter[0] < t - 3000:
            self.counter.pop(0)
        return len(self.counter)

# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
a = obj.ping1(1)
b = obj.ping1(100)
c = obj.ping1(3001)
d = obj.ping1(3002)
print(a, b, c, d)