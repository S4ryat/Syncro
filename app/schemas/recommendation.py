from typing import Optional
from pydantic import UUID4, BaseModel

class RecommendationBase(BaseModel):
    user_id: Optional[UUID4] = None
    music_id: Optional[UUID4] = None

class RecommendationCreate(RecommendationBase):
    user_id: UUID4
    music_id: UUID4

class RecommendationUpdate(RecommendationBase):
    pass

class RecommendationInDBBase(RecommendationBase):
    id: Optional[UUID4] = None

    class Config:
        orm_mode = True

class Recommendation(RecommendationInDBBase):
    pass

class RecommendationInDB(RecommendationInDBBase):
    pass
