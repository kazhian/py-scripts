from dataclasses import dataclass

@dataclass
class Movie:
    title: str
    year: int
    rating: int

    def __str__(self):
        return f"{self.title} ({self.year}) - {self.rating}/10"

coolie = Movie(title="Coolie", year=2020, rating=8)
print(coolie)

coolie['rating'] = 3.5
print(coolie)

# Run: python -m typesafe_dataclass
# you will get error
#     coolie['rating'] = 3.5
#     ~~~~~~^^^^^^^^^^
# TypeError: 'Movie' object does not support item assignment
