"""fraktion as enum

Revision ID: 153d2b8ee92e
Revises: d733351f5e0f
Create Date: 2025-01-26 09:10:09.000466

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy import Enum


# revision identifiers, used by Alembic.
revision: str = '153d2b8ee92e'
down_revision: Union[str, None] = 'd733351f5e0f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Define the Enum type that will be used in the database
    fraktion_enum = Enum('CDU', 'SPD', 'GRUENE', 'FDP', 'DIE_LINKE', 'AfD', 'BSW', 'OTHER', name='fraktion')

    # Ensure the Enum type 'fraktion' is created (if not already done)
    op.execute("""
        DO $$ BEGIN
            IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'fraktion') THEN
                CREATE TYPE fraktion AS ENUM ('CDU', 'SPD', 'GRUENE', 'FDP', 'DIE_LINKE', 'AfD', 'BSW', 'OTHER');
            END IF;
        END $$;
    """)

    # Alter the column 'fraktion' in the 'redner' table to use the 'fraktion' Enum type
    op.alter_column('redner', 'fraktion',
                    existing_type=sa.VARCHAR(),
                    type_=fraktion_enum,
                    existing_nullable=True,
                    postgresql_using='fraktion::fraktion')


def downgrade() -> None:
    # In the downgrade method, we revert back to a VARCHAR column
    op.alter_column('redner', 'fraktion',
                    existing_type=sa.Enum('CDU', 'SPD', 'GRUENE', 'FDP', 'DIE_LINKE', 'AfD', 'BSW', 'OTHER', name='fraktion'),
                    type_=sa.VARCHAR(),
                    existing_nullable=True)

    # Drop the 'fraktion' enum type, if it's no longer in use
    op.execute("DROP TYPE IF EXISTS fraktion")