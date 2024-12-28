from db.session import Base

from sqlalchemy import Column, Boolean, Text


class YCRVacancies(Base):
    __tablename__ = 'YCRVacancies'

    active = Column(Boolean, nullable=False)
    description = Column(Text, nullable=False)
