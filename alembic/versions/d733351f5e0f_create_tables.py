"""Create tables

Revision ID: d733351f5e0f
Revises: 
Create Date: 2025-01-25 22:14:58.136724

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd733351f5e0f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rolle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rolle_lang', sa.String(), nullable=True),
    sa.Column('rolle_kurz', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sitzung',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('wahlperiode', sa.Integer(), nullable=False),
    sa.Column('sitzungsnummer', sa.Integer(), nullable=False),
    sa.Column('datum', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('name',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titel', sa.String(), nullable=True),
    sa.Column('vorname', sa.String(), nullable=True),
    sa.Column('nachname', sa.String(), nullable=True),
    sa.Column('namenszusatz', sa.String(), nullable=True),
    sa.Column('ortszusatz', sa.String(), nullable=True),
    sa.Column('fraktion', sa.String(), nullable=True),
    sa.Column('rolle_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['rolle_id'], ['rolle.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('redner',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('redner_id', sa.String(), nullable=False),
    sa.Column('name_id', sa.Integer(), nullable=True),
    sa.Column('fraktion', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['name_id'], ['name.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('redner_id')
    )
    op.create_table('rede',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('rede_id', sa.String(), nullable=False),
    sa.Column('sitzung_id', sa.Integer(), nullable=True),
    sa.Column('rede_text', sa.String(), nullable=True),
    sa.Column('redner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['redner_id'], ['redner.id'], ),
    sa.ForeignKeyConstraint(['sitzung_id'], ['sitzung.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('rede_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rede')
    op.drop_table('redner')
    op.drop_table('name')
    op.drop_table('sitzung')
    op.drop_table('rolle')
    # ### end Alembic commands ###
