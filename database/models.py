from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# Base para las clases de modelo
Base = declarative_base()

# Creación del motor de la base de datos SQLite
engine = create_engine('sqlite:///club_management.db')

# Configuración de la sesión
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
session = SessionLocal()

# Modelo para los miembros (socios)
class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)
    role = Column(String, default="user")
    balance = Column(Integer, default=0)

    # Relación con consumos
    consumptions = relationship("Consumption", back_populates="member")

    # Relación con entradas y salidas
    entries = relationship("Entry", back_populates="member")

# Modelo para los registros de entrada/salida
class Entry(Base):
    __tablename__ = 'entries'

    id = Column(Integer, primary_key=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    time = Column(DateTime, default=datetime.now)
    entry_type = Column(String)  # 'entry' or 'exit'

    # Relación con consumos
    consumptions = relationship("Consumption", back_populates="entry")

    member = relationship("Member", back_populates="entries")

# Modelo para los registros de consumiciones
class Consumption(Base):
    __tablename__ = "consumptions"

    id = Column(Integer, primary_key=True, index=True)
    member_id = Column(Integer, ForeignKey('members.id'))
    entry_id = Column(Integer, ForeignKey('entries.id'))
    date = Column(DateTime, default=datetime.now)
    amount = Column(Integer)

    # Relación con el miembro
    member = relationship("Member", back_populates="consumptions")

    # Relación con la entrada
    entry = relationship("Entry", back_populates="consumptions")

# Inicialización de la base de datos
def init_db():
    Base.metadata.create_all(engine)
