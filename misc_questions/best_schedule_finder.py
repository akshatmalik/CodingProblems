class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.closed = True  # by default, the interval is closed
    # set the flag for closed/open

    def set_closed(self, closed):
        self.closed = closed

    def __str__(self):
        return "[" + str(self.start) + ", " + str(self.end) + "]" \
            if self.closed else \
                "(" + str(self.start) + ", " + str(self.end) + ")"


schedule = [[[1,2],[5,6]],[[1,3]],[[4,10]]]

"""
1. number of employees - 
2. array, [min, mix]
    a) in this interval, who all are busy
3. find intervals no one is busy

1. in case we increase the granularity of the time slots, right now it is 1hr

1. its all busy time right now, we convert it to free time
"""

def employee_free_time(schedule):

    number_of_employees = len(schedule)
    print(f"number_of_employees {number_of_employees}")

    min_start, max_end = 10000000, -1
    for i in range(number_of_employees):
        for interval_start, interval_end in schedule[i]:
            if interval_start < min_start:
                min_start = interval_start
            if interval_end > max_end:
                max_end = interval_end

    print(f"min_start {min_start} max_end {max_end}")
    schedule_holder = [[] for _ in range(max_end)]

    print(schedule_holder)

    for emp_num in range(number_of_employees):
        for interval_start, interval_end in schedule[emp_num]:
            print(f"emplyo {emp_num} interval_start {interval_start} interval_end {interval_end}")
            for i in range(interval_start, interval_end):
                print(f"adding to i {i}")
                schedule_holder[i].append(emp_num)

    print(schedule_holder)
    for i in range(min_start, max_end):
        if len(schedule_holder[i]) == 0:
            print(f"hour {i} - {i+1}")





    return []


employee_free_time(schedule)