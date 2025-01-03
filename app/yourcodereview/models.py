from db.session import Base

from sqlalchemy import Text
from sqlalchemy.orm import Mapped, mapped_column


class YCRVacancies(Base):
    __tablename__ = 'YCRVacancies'

    active: Mapped[bool]
    description: Mapped[str] = mapped_column(Text)
