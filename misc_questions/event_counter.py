"""
we're going to build an event counter

# increments the counter associated / event_name
# time is seconds from the unix epoch
record(event_name: str, time: int) -> ()

# query is going to return an aggregated view of the event counts
# start and end are inclusive and exclusive respectively
# they are specified in units of resolution from the epoch
# if there aren't events, fill list with 0 (because we're returning counts!)
query(event_name: str, resolution: hour | day, start: int, end: int) -> []int

record("page_view/index.html", 0)
record("page_view/index.html", 1)
record("page_view/index.html", 3600)
record("page_view/index.html", 24 * 3600)

query("page_view/index.html", "hour", 0, 3) -> [2, 1, 0]
query("page_view/index.html", "day", 0, 3) -> [3, 1, 0]

1. check for start and end




{
    "page_view/index.html" : {
        hour_0 : 1
        hour_1 =

    }
}


record("page_view/index.html", 0)
"""


class EventCounter:

    def __init__(self):
        self.event_store = {}

    def __calculate_hour(self, time: int) -> str:

        hour_increment = 60 * 60

        return f"hour_{time // hour_increment}"

    def record(self, event_name: str, time: int) -> None:

        # recording the event for the first time
        if event_name not in self.event_store:
            self.event_store[event_name] = {}

        hour_increment = self.__calculate_hour(time)
        # print(f"hour_increment - {hour_increment}")

        if hour_increment not in self.event_store[event_name]:
            self.event_store[event_name][hour_increment] = 0

        self.event_store[event_name][hour_increment] += 1
        # print(self.event_store)

    def query(self, event_name: str, resolution: str, start: int, end: int) -> []:

        if resolution != "hour":
            raise Exception(f"Invalid resolution {resolution}")

        event_recorded = [0 for _ in range(start, end)]
        # print(event_recorded)

        for hour in range(start, end):

            index_key = hour - start
            hour_key = f"hour_{hour}"
            # TODO: iterate over hour keys and add events
            if hour_key not in self.event_store[event_name]:
                continue
            event_recorded[index_key] = self.event_store[event_name][hour_key]

        print(event_recorded)
        return event_recorded


if __name__ == "__main__":

    event_calculator = EventCounter()

    event_calculator.record("hello", 2)
    event_calculator.record("hello", 2 * 60 * 60 + 4)

    event_calculator.query("hello", "hour", 0, 1)
    event_calculator.query("hello", "hour", 0, 2)
    event_calculator.query("hello", "hour", 0, 3)





