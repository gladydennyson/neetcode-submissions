class TimeMap:

    def __init__(self):
        self.store = {}


    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = [(value, timestamp)]
        else:
            self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:

        # first we should check if timestamp exists or not in the value
        # if yes, return it
        values = self.store.get(key, [])
        l = 0 
        r = len(values) - 1
        m = 0
        res = ""
        while l <= r:
            m = (l + r) // 2
            if int(values[m][1]) == timestamp:
                return values[m][0]
            elif int(values[m][1]) < timestamp:
                res = values[m][0]  # save closest valid answer
                l = m + 1
            else :
                 r = m - 1
        return res

        
