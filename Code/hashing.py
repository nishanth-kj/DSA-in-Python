class Hashing:
    def __init__(self, arr):
        self.arr = arr
        self.freq = {}
        self.max_freq = float('-inf')
        self.min_freq = float('inf')
        self.max_key = None
        self.min_key = None

        self.frequency()
        self.high_frequency_and_lowest_frequency()

    def frequency(self):
        for i in self.arr:
            if i not in self.freq:
                self.freq[i] = 1
            else:
                self.freq[i] += 1

    def high_frequency_and_lowest_frequency(self):
        for key, value in self.freq.items():
            if value > self.max_freq:
                self.max_freq = value
                self.max_key = key

            if value < self.min_freq:
                self.min_freq = value
                self.min_key = key


if __name__ == "__main__":
    arr = []
    n = int(input("Enter the size of the list: "))
    for _ in range(n):
        arr.append(input("Enter the value: "))

    hashing = Hashing(arr)

    print(f"Frequency Map       : {hashing.freq}")
    print(f"Lowest Frequency    : {hashing.min_freq}")
    print(f"Lowest Freq Element : {hashing.min_key}")
    print(f"Highest Frequency   : {hashing.max_freq}")
    print(f"Highest Freq Element: {hashing.max_key}")
