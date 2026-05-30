class TimeMap:

    def __init__(self):
        self.mapper = defaultdict(dict)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mapper[key][timestamp] = value
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mapper:
            return ''

        if timestamp in self.mapper[key]:
            return self.mapper[key][timestamp]

        for timestamp_prev in range(timestamp - 1, -1, -1):
            if timestamp_prev in self.mapper[key]:
                return self.mapper[key][timestamp_prev]

        return ''
