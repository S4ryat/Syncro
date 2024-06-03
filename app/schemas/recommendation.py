from pydantic import BaseModel, UUID4
from typing import Optional

class RecommendationBase(BaseModel):
    user_id: UUID4
    music_id: UUID4
    comment: Optional[str] = None

class RecommendationCreate(RecommendationBase):
    pass

class RecommendationUpdate(RecommendationBase):
    pass

class Recommendation(RecommendationBase):
    id: UUID4

    class Config:
        orm_mode = True
