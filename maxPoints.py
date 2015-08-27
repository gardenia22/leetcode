# Definition for a point.
class Point:

    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    # @param {Point[]} points
    # @return {integer}

    def maxPoints(self, points):
        if not points:
            return 0
        ans = 1
        for i, p1 in enumerate(points):
            count = {}
            numPoint = 1
            for j, p2 in enumerate(points[i+1:]):
                gradient = self.gradient(p1, p2)
                if gradient != "same":
                    count[gradient] = count.get(gradient, 0) + 1
                else:
                    numPoint += 1
            if count:
                numPoint += max(count.values())
            ans = max(ans, numPoint)
        return ans

    def gradient(self, p1, p2):
        if p1.y != p2.y:
            return (p1.x-p2.x)*1.0/(p1.y-p2.y)
        elif p1.x != p2.x:
            return "Inf"
        else:
            return "same"
# points = [Point(1,3),Point(1,1),Point(0,0),Point(2,2)]
# points = [Point(-54,-297),Point(-36,-222),Point(3,-2),Point(30,53),Point(-5,1),Point(-36,-222),Point(0,2),Point(1,3),Point(6,-47),Point(0,4),Point(2,3),Point(5,0),Point(48,128),Point(24,28),Point(0,-5),Point(48,128),Point(-12,-122),Point(-54,-297),Point(-42,-247),Point(-5,0),Point(2,4),Point(0,0),Point(54,153),Point(-30,-197),Point(4,5),Point(4,3),Point(-42,-247),Point(6,-47),Point(-60,-322),Point(-4,-2),Point(-18,-147),Point(6,-47),Point(60,178),Point(30,53),Point(-5,3),Point(-42,-247),Point(2,-2),Point(12,-22),Point(24,28),Point(0,-72),Point(3,-4),Point(-60,-322),Point(48,128),Point(0,-72),Point(-5,3),Point(5,5),Point(-24,-172),Point(-48,-272),Point(36,78),Point(-3,3)]
points = [Point(0, 9), Point(138, 429), Point(115, 359), Point(115, 359), Point(-30, -102), Point(230, 709), Point(-150, -686), Point(-135, -613), Point(-60, -248), Point(-161, -481),
          Point(207, 639), Point(23, 79), Point(-230, -691), Point(-115, -341), Point(92, 289), Point(60, 336), Point(-105, -467), Point(135, 701), Point(-90, -394), Point(-184, -551), Point(150, 774)]
a = Solution()
print a.maxPoints(points)
