from ratingsystem import FoodRatings
import pytest

# FoodRatings foodRatings = new
# FoodRatings(["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"], ["korean", "japanese", "japanese", "greek", "japanese", "korean"], [9, 12, 8, 15, 14, 7]);


#     def changeRating(self, food: str, newRating: int) -> None:


#     def highestRated(self, cuisine: str) -> str:


# [
#     "FoodRatings",
#     "highestRated",
#     "highestRated",
#     "changeRating",
#     "highestRated",
#     "changeRating",
#     "highestRated",
# ]
# [
#     [
#         ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
#         ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
#         [9, 12, 8, 15, 14, 7],
#     ],
#     ["korean"],
#     ["japanese"],
#     ["sushi", 16],
#     ["japanese"],
#     ["ramen", 16],
#     ["japanese"],
# ]
# Output
# [null, "kimchi", "ramen", null, "sushi", null, "ramen"]


@pytest.mark.parametrize("cuisine, expected", [("korean", 9), ("japanese", 14)])
def test_highest_rated(cuisine, expected):
    food_ratings = FoodRatings(
        ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        [9, 12, 8, 15, 14, 7],
    )

    assert food_ratings.highestRated(cuisine) == expected


@pytest.mark.parametrize("cuisine, expected", [("korean", 9), ("japanese", 14)])
def test_change_rating(cuisine, expected):
    food_ratings = FoodRatings(
        ["kimchi", "miso", "sushi", "moussaka", "ramen", "bulgogi"],
        ["korean", "japanese", "japanese", "greek", "japanese", "korean"],
        [9, 12, 8, 15, 14, 7],
    )

    assert food_ratings.highestRated("japanese") == 14

    food_ratings.changeRating("sushi", 200)

    assert food_ratings.highestRated("japanese") == 200
