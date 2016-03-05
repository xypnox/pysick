class data:
    def __init__(self, kind, data=0, freq=0):
        if kind == 'raw':
            self.raw = data
            self.kind = kind

        elif kind == "continuous" or kind == "cont":  # cont is only for ease
            self.limits = data  # upper and lower limits
            self.freq = freq  # respective frquencies
            self.kind = 'continuous'

        elif kind == 'discrete' or kind == 'dsc':
            self.limits = data  # upper and lower limits
            self.freq = freq  # respective frquencies
            self.kind = 'discrete'

    def display(self):
        if self.kind == 'raw':
            print(self.raw)

        elif self.kind == "continuous" or self.kind == 'discrete':
            for i in range(len(self.freq)):
                print(self.limits[i], ' \t', self.freq[i])

    def average(self):
        if self.kind == 'raw':
            return sum(self.raw)/len(self.raw)

        elif self.kind == 'continuous' or self.kind == 'discrete':
            mean = 0
            for i in range(len(self.limits)):
                mean += sum(self.limits[i])/2 * self.freq[i]
            mean /= sum(self.freq)
            return mean

    def deviation(self, around='mean'):
        if around == 'mean':
            var = self.average()

        if self.kind == 'raw':
            dvt = 0
            for i in self.raw:
                dvt += abs(i - var)
            dvt /= len(self.raw)
        elif self.kind == 'continuous':
            dvt = 0  # deviation
            for i in range(len(self.freq)):
                dvt += self.freq[i]*abs((sum(self.limits[i])/2) - var)
            dvt /= sum(self.freq)
        return dvt

    def organize(self, height, order='continuous'):
        if self.kind == 'raw':
            raw = self.raw
            raw.sort()
            if order == 'continuous' or order == 'cont':
                lowerlimit = raw[0] - raw[0] % height
                upperlimit = lowerlimit
                limits, freq = [], []
                while max(raw) > upperlimit:
                    upperlimit = lowerlimit + height
                    limits.append([lowerlimit, upperlimit])
                    k = 0
                    for i in raw:
                        if i in range(lowerlimit, upperlimit):
                            k += 1
                    freq.append(k)
                    lowerlimit += height
                self.limits = limits
                self.freq = freq
                self.kind = 'continuous'

# tests

# marks = data(
#     'dsc',
#     [
#         [1, 10], [11, 20], [21, 30], [31, 40], [41, 50]
#     ],
#     [2, 4, 6, 5, 3]
# )
#
# marksc = data(
#     'cont',
#     [
#         [0, 10], [10, 20], [20, 30], [30, 40], [40, 50]
#     ],
#     [2, 4, 6, 5, 3]
# )

runs = data(
    'raw',
    [2, 4, 3, 6, 8, 13, 7, 8, 20, 5, 6, 14, 8, 9, 4, 13, 8, 22, 4, 1]
)

runs.display()
print(runs.deviation())
print(runs.average())

runs.organize(5)

runs.display()
print(runs.deviation())
print(runs.average())
