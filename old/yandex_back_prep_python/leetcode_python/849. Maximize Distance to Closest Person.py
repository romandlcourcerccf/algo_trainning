class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        l = r = 0
        max_distance = float("-inf")

        while r < len(seats):
            if seats[r] == 0:
                l = r
                while r < len(seats) - 1 and seats[r] == seats[r + 1]:
                    r += 1

                if l == 0:
                    max_distance = max(max_distance, r - l + 1)
                elif r == len(seats) - 1:
                    max_distance = max(max_distance, r - l + 1)
                else:
                    max_distance = max(max_distance, int((r + 1) - (r + l) / 2))

                r += 1
                l = r
            else:
                r += 1
                l += 1

        return max_distance
