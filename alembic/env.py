from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncConnection
from alembic import context
from app.models import Base
from dotenv import load_dotenv
import os
import asyncio
from app.database import Base

# Charger les variables d'environnement
load_dotenv()

# URL de la base de données
DATABASE_URL = f"postgresql+asyncpg://{os.getenv('DATABASE_USER')}:{os.getenv('DATABASE_PASSWORD')}@{os.getenv('DATABASE_HOST')}:{os.getenv('DATABASE_PORT')}/{os.getenv('DATABASE_NAME')}"

print(f"DATABASE_URL: {DATABASE_URL}")  # To debug the entire URL
print(f"DATABASE_PASSWORD: {os.getenv('DATABASE_PASSWORD')}")

# Créer un moteur async
connectable = create_async_engine(DATABASE_URL, echo=True)

# Configuration de logging
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Configuration pour autogenerate
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Exécuter les migrations en mode 'offline'.

    Ce mode ne nécessite pas de connexion active à la base de données.
    """
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


async def run_migrations_online():
    """Exécuter les migrations en mode 'online'.

    Utilise une connexion async au moteur.
    """
    async with connectable.connect() as connection:
        await connection.run_sync(
            lambda sync_connection: context.configure(
                connection=sync_connection,
                target_metadata=target_metadata,
            )
        )
        await connection.run_sync(
            lambda sync_connection: context.run_migrations()
        )


if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
