class Date():
    def __init__(self, y, m, d):
        self.y = y
        self.m = m
        self.d = d

    def show(self):
        print(self.y,"/",self.m,"/",self.d)

    def sum(self,d):
        result = Date(None,None,None)
        result.y = self.y + d.y
        result.m = self.m + d.m
        result.d = self.d + d.d
        if result.m > 12 :
            result.m -= 12
            result.y += 1
        if result.d > 30:
            result.d -= 30
            result.m += 1
        return result

    def sub(self, d):
        result = Date(None,None,None)
        result.y = self.y - d.y
        result.m = self.m - d.m
        result.d = self.d - d.d
        if result.m < 0 :
            result.m += 12
            result.y -= 1
        if result.d < 0:
            result.d += 30
            result.m -= 1
        if result.y < 0:
            result.y = -(result.y)
        return result

date1 = Date(2020, 1, 31)
date2 = Date(2022, 11, 11)

result_sum = date1.sum(date2)
print("Date sum: ")
result_sum.show()