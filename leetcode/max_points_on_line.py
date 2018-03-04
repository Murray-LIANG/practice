from __future__ import division
import decimal
# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b

    def __str__(self):
        return '(x={}, y={})'.format(self.x, self.y)

    def __repr__(self):
        return '(x={}, y={})'.format(self.x, self.y)

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)

        max_z = 0
        for i in range(len(points)):
            same_point = 1

            tmp = {}
            for j in range(i+1, len(points)):
                dx = points[j].x - points[i].x
                dy = points[j].y - points[i].y
                if dx == 0 and dy == 0:
                    # Skip the same point
                    same_point += 1
                    continue
                elif dx == 0:
                    tmp['+'] = tmp['+'] + 1 if '+' in tmp else 1
                else:
                    c = self.gcd(dy, dx)
                    r = (dy / c, dx / c)
                    tmp[r] = tmp[r] + 1 if r in tmp else 1
            max_tmp = max(tmp.values()) if tmp else 0
            max_z = max(max_z, max_tmp + same_point)

        return max_z

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a%b)


if __name__ == '__main__':
    datas = [
        ((), 0),
        (([1,2],), 1),
        (([1,2], [1,2]), 2),
        (([1,2], [1,2], [2,4], [2,4]), 4),
        (([1,2], [1,2], [1,2]), 3),
        (([1,2], [2,4]), 2),
        (([1,2], [2,4], [1,3], [1,4]), 3),
        (([1,2], [2,4], [1,2], [1,4]), 3),
        (([84,250],[0,0],[1,0],[0,-70],[0,-70],[1,-1],[21,10],[42,90],[-42,-230]), 6),
        (([0,0],[94911151,94911150],[94911152,94911151]), 2),
    ]

    for ps, expected in datas:
        points = []
        for p in ps:
            points.append(Point(p[0], p[1]))

        result = Solution().maxPoints(points)
        print('points: {}. Result: {}. Expected: {}'.format(
            points, result, expected == result))
