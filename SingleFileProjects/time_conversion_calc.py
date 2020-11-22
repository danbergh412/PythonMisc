import sys

class Time:
    def __init__(self, totalSeconds):
        secondsToDays = (60 * 60 * 24);
        secondsToHours = (60 * 60);
        secondsToMinutes = 60;

        self.days = totalSeconds // secondsToDays
        totalSeconds = totalSeconds % secondsToDays

        self.hours = totalSeconds // secondsToHours
        totalSeconds = totalSeconds % secondsToHours

        self.minutes = totalSeconds // secondsToMinutes

        self.seconds = totalSeconds % secondsToMinutes
    def __str__(self):
        return str(self.days) + ' days ' + str(self.hours) + ' hours ' + str(self.minutes) + ' minutes ' + str(self.seconds) + ' seconds'

if len(sys.argv) > 1:
    seconds = sys.argv[1]
else:
    seconds = input("Enter time in seconds:")

seconds = int(seconds)
print(Time(seconds))
