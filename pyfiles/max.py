 def computeDifference(self):
        m1=0
        for i in self.__elements:
                if i>m1:
                    m1=i
        m2=self.__elements[0]
        for i in self.__elements:
                if i<m2:
                    m2=i
        m3=m1-m2
        self.maximumDifference=m3
# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
