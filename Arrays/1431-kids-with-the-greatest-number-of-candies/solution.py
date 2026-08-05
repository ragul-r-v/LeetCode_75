class Solution:
    def kidsWithCandies(self, candies, extraCandies):
        maximum = max(candies)

        answer = []

        for candy in candies:
            if candy + extraCandies >= maximum:
                answer.append(True)
            else:
                answer.append(False)

        return answer
