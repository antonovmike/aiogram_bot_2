from sqlalchemy import BigInteger
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

from config import SQLALCHEMY_URL

engine = create_async_engine(SQLALCHEMY_URL, echo=True)

async_session = async_sessionmaker(engine)


class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id: Mapped[int] = mapped_column(BigInteger)
    name: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    orders: Mapped[list] = relationship('Order', back_populates='user')

    def __repr__(self):
        return f'<Eser {self.name}>'
