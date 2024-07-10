# database_init.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Base de datos para desarrollo
SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
# Base de datos para producción
#SQLALCHEMY_DATABASE_URL = "sqlite:///club_management.db"

# Configuración de la conexión a la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Función para inicializar la base de datos
def init_db():
    Base.metadata.create_all(bind=engine)

# Declaración de la clase Base para la definición de modelos
Base = declarative_base()

# Función para obtener una sesión de base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
