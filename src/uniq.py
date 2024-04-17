import sys
import os
class UniqChecker:

    def __init__(self):
        self.known = {}
        self.max_cache = 10
        self.savefile = os.path.join(os.path.dirname(__file__), "uniqsave.txt")

    def flush_to_disk(self):
        to_remove = self.lru()
        with open(self.savefile, 'a') as f:
            f.write(f"{to_remove}\n")
        del self.known[to_remove]
        pass

    def check_cache_full(self):
        if len(self.known) > self.max_cache:
            self.flush_to_disk()

    def check_disk(self, input):
        if os.path.exists(self.savefile):
            with open(self.savefile, 'r') as f:
                entry = f.readline().strip("\n")
                if entry == input:
                    return True
        return False

    def handle(self, input):
        if input in self.known:
            self.known[input] += 1
            return None
        if self.check_disk(input):
            return None
        self.known[input] = 1
        self.check_cache_full()
        return input
    
    def lru(self):
        keys = list(self.known.keys())
        keys.reverse()
        if not len(keys):
            return None
        min_key = keys.pop()
        min_val = self.known[min_key]
        for key in keys:
            value = self.known[key]
            if value < min_val:
                min_key, min_val = key, value
        return min_key

def main():

    checker = UniqChecker()

    for line in sys.stdin:
        to_print = checker.handle(line.rstrip("\n"))
        if to_print is not None:
            print(to_print)

if __name__ == "__main__":
    main()