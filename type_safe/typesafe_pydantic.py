from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import ClassVar

class Movie(BaseModel):
    model_config = {
        "validate_assignment": True,  # Enable validation on attribute assignment
        "frozen": False,             # Allow modifications but validate them
    }
    
    title: str
    year: int = Field(..., gt=1900, lt=2100)  # Year between 1900-2100
    rating: float = Field(..., ge=0, le=10)   # Rating between 0-10
    
    def __str__(self):
        return f"{self.title} ({self.year}) - {self.rating:.1f}/10"

# Example usage
print("Creating valid movie:")
try:
    coolie = Movie(title="Coolie", year=2020, rating=8.5)
    print(f"Created: {coolie}")
except ValidationError as e:
    print(f"Error creating movie: {e}")
    exit(1)

print("\nTrying to set invalid rating:")
try:
    coolie.rating = 11  # This should now raise a ValidationError
    print(f"Updated: {coolie}")
except ValidationError as e:
    print(f"Error updating rating: {e}")
    print(f"Current movie state: {coolie}")

# Run: python -m typesafe_pydantic
