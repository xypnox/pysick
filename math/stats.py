class data:
    """
    Data Class:
    This class is complete data management tool.
    It stores raw or class(ed) data.

    It has the following methods available:
        obj.display()
            display the data
        obj.average()
            Arithmetic mean
        obj.deviation(<around>)
            Deviation around the passed argument, default = mean
        obj.organize(height)
            Organize the data passed into class intervals
    """
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
                mean += sum(self.limits[i])/2 * self.freq[i]  # freq * classMid
            mean /= sum(self.freq)
            return mean

    def deviation(self, around='mean'):
        if around == 'mean':
            midvalue = self.average()

        if self.kind == 'raw':
            dvt = 0
            for i in self.raw:
                dvt += abs(i - midvalue)
            dvt /= len(self.raw)
        elif self.kind == 'continuous':
            dvt = 0  # deviation
            for i in range(len(self.freq)):
                dvt += self.freq[i]*abs((sum(self.limits[i])/2) - midvalue)
            dvt /= sum(self.freq)
        return dvt

    def variance(self, around='mean'):
        if around == 'mean':
            midvalue = self.average()

        if self.kind == 'raw':
            var = 0
            for i in self.raw:
                var += (i - midvalue) ** 2
            var /= len(self.raw)
        elif self.kind == 'continuous':
            var = 0  # deviation
            for i in range(len(self.freq)):
                var += self.freq[i] * ((sum(self.limits[i])/2) - midvalue) ** 2
            var /= sum(self.freq)
        return var

    def standardDeviation(self, around='mean'):
        return self.variance(around)**(1/2)

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
# marksc = data(
#     'cont',
#     [
#         [0, 10], [10, 20], [20, 30], [30, 40], [40, 50]
#     ],
#     [2, 4, 6, 5, 3]
# )

runs_india = data(
    'raw',
    [2, 4, 3, 6, 8, 13, 7, 8, 20, 5, 6, 14, 8, 9, 4, 13, 8, 22, 4, 1]
)

runs_pakistan = data(
    'raw',
    [2, 4, 5, 6, 4, 3, 1, 5, 0, 6, 3, 5, 3, 4, 3, 5, 2, 4, 2, 4]
)

print('India')
runs_india.display()
print('mean =', runs_india.average())
print('deviation =', runs_india.deviation())
print('variance =', runs_india.variance())
print('Standard Deviation =', runs_india.standardDeviation())

print('\nPakistan')
runs_pakistan.display()
print('mean =', runs_pakistan.average())
print('deviation =', runs_pakistan.deviation())
print('variance =', runs_pakistan.variance())
print('Standard Deviation =', runs_pakistan.standardDeviation())
