from typing import List
from collections import defaultdict

import heapq


class FoodRatings:
    def __init__(
        self, foods: List[str], cuisines: List[str], ratings: List[int]
    ) -> None:
        self.ratings = defaultdict(list)
        self.food_cuisine = {}

        for idx, cuisine in enumerate(cuisines):
            self.food_cuisine[foods[idx]] = cuisines[idx]

        for idx, cuisine in enumerate(cuisines):
            self.ratings[cuisine].append((-ratings[idx], foods[idx]))

        for cuisine in self.ratings:
            heapq.heapify(self.ratings[cuisine])

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine = self.food_cuisine[food]
        self.ratings[cuisine].append((-newRating, food))
        heapq.heapify(self.ratings[cuisine])

    def highestRated(self, cuisine: str) -> str:
        print(self.ratings)
        return -self.ratings[cuisine][0][0]
