from pydantic import BaseModel

class ListFood(BaseModel):
    strMeal: str
    strMealThumb: str
    idMeal: str
    
    
class FoodMain(BaseModel):
    strMeal: str
    strMealThumb: str
    strInstructions: str
    ingredients: dict
    measure: dict