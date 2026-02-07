from pydantic import BaseModel, Field

class CustomerData(BaseModel):
    # Inputs based on your dataset columns (its good not just the user errors its good for security
        #i was Bug bonty hunter lol)
    gender: str = Field(..., example="Male")
    age: int = Field(..., ge=18, le=100, example=30)
    city: str = Field(..., example="New York")
    membership_type: str = Field(..., example="Gold")
    total_spend: float = Field(..., example=500.0)
    items_purchased: int = Field(..., example=10)
    average_rating: float = Field(..., example=4.5)
    discount_applied: bool = Field(..., example=True)
    days_since_last_purchase: int = Field(..., example=5)

class PredictionResponse(BaseModel):
    # Output structure
    satisfaction_score: str 
    probability: float
    alert_level: str
    action_required: str