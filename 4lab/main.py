

if __name__ == "__main__":
    pass 

class HMSInterval:
    def __init__(self, h, m, s):
        self.h = h
        self.m = m
        self.s = s

    def to_seconds(self):
        return self.h * 3600 + self.m * 60 + self.s


class MSInterval:
    def __init__(self, ms):
        self.ms = ms

    def to_seconds(self):
        return self.ms / 1000


class MinSecInterval:
    def __init__(self, m, s):
        self.m = m
        self.s = s

    def to_seconds(self):
        return self.m * 60 + self.s


class HoursFloatInterval:
    def __init__(self, hours):
        self.hours = hours

    def to_seconds(self):
        return self.hours * 3600



def seconds_to_hms(seconds):
    seconds = int(seconds)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02d}:{m:02d}:{s:02d}"


def seconds_to_human(seconds):
    seconds = int(seconds)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h} h {m} min {s} s"


def total_seconds(intervals):
    return sum(i.to_seconds() for i in intervals)


def average_seconds(intervals):
    return total_seconds(intervals) / len(intervals)


def min_interval(intervals):
    return min(intervals, key=lambda i: i.to_seconds())


def max_interval(intervals):
    return max(intervals, key=lambda i: i.to_seconds())



intervals = [
    HMSInterval(1, 30, 0),  
    MSInterval(90000),      
    MinSecInterval(3, 45),    
    HoursFloatInterval(2.5),  
]

total = total_seconds(intervals)
avg = average_seconds(intervals)
min_i = min_interval(intervals)
max_i = max_interval(intervals)

print(f"Total: {seconds_to_human(total)} ({int(total)} s, {seconds_to_hms(total)})")
print(f"Average: {seconds_to_human(avg)} ({int(avg)} s, {seconds_to_hms(avg)})")
print(f"Min: {seconds_to_human(min_i.to_seconds())} "
      f"({int(min_i.to_seconds())} s, {seconds_to_hms(min_i.to_seconds())})")
print(f"Max: {seconds_to_human(max_i.to_seconds())} "
      f"({int(max_i.to_seconds())} s, {seconds_to_hms(max_i.to_seconds())})")
