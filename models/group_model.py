from typing import Dict, Union

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from .base import Base
from .student_model import Student


class Group(Base):
    __tablename__ = 'group'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    id_group: Student = relationship('Student')

    def to_dict(self) -> Dict[Union[int, str, None], Union[int, str, None] | Student]:
        return dict(
            id=self.id,
            name=self.name,
            id_group=self.id_group
        )
