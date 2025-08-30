from typing import TypedDict

class Movie(TypedDict):
    title: str
    year: int
    rating: int

    # This is not valid TypedDict syntax
    # TypedDict should be used only when your class is going to act dictionary
    def __str__(self):

        return f"{self.title} ({self.year}) - {self.rating}/10"

coolie = Movie(title="Coolie", year=2020, rating=8)
print(coolie)

coolie['rating'] = 3.5
print(coolie)

# Run: mypy typesafe_typeddict.py
# You will get error
# typesafe_typeddict.py:8: error: Invalid statement in TypedDict definition; expected "field_name: field_type"  [misc]
# typesafe_typeddict.py:14: error: Value of "rating" has incompatible type "float"; expected "int"  [typeddict-item]
# Found 2 errors in 1 file (checked 1 source file)
