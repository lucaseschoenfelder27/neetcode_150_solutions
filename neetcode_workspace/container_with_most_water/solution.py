from itertools import combinations

class Solution:
    # Time: O(?)
    # Space: O(?)
    def max_area(self, height: list[int]) -> int:
        # TODO: Implement max_area
        points = [{"x": i+1, "y": h} for i, h in enumerate(height)]
        possible_combinations = list(combinations(points, 2))
        max_area = 0
        for possible in possible_combinations:
            xaxis = abs(possible[0]["x"] - possible[1]["x"])
            yaxis = min(possible[0]["y"], possible[1]["y"])
            area = xaxis * yaxis
            if area > max_area:
                max_area = area
        return max_area
 