from typing import Dict, Union

from sqlalchemy import Column, Integer, String

from .base import Base


class Course(Base):
    __tablename__ = 'course'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(200))

    def to_dict(self) -> Dict[str, Union[int, None, str]]:
        return dict(
            id=self.id,
            name=self.name,
            description=self.description
        )
