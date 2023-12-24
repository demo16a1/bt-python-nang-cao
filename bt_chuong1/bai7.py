
class Date:
    def __init__(self, day = 1, month = 1, year = 2004):
        self.day = day
        self.month = month
        self.year = year
        
    def display(self):
        print("ngày {} tháng {} năm {}".format(self.day, self.month, self.year))

    def next(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.month == 2 and ((self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)):
            days_in_month[1] = 29
        if self.day < days_in_month[self.month - 1]:
            self.day += 1
        else:
            self.day = 1
            if self.month == 12:
                self.month = 1
                self.year += 1
            else:
                self.month += 1
#--------------------------------------
d = Date(24,12,2023)
d.display() 
d.next()
d.display()