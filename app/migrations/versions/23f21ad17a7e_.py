"""empty message

Revision ID: 23f21ad17a7e
Revises: 77a686430247
Create Date: 2024-07-29 09:32:20.832038

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '23f21ad17a7e'
down_revision: Union[str, None] = '77a686430247'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transazioni_esterne',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('iban', sa.String(length=27), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transazioni_interne',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('conto_corrente_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['conto_corrente_id'], ['conti_correnti.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('transazioni',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('importo', sa.Integer(), nullable=True),
    sa.Column('data', sa.DateTime(), nullable=True),
    sa.Column('entrata', sa.Boolean(), nullable=True),
    sa.Column('transazione_interna_id', sa.Integer(), nullable=True),
    sa.Column('transazione_esterna_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['transazione_esterna_id'], ['transazioni_esterne.id'], ),
    sa.ForeignKeyConstraint(['transazione_interna_id'], ['transazioni_interne.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transazioni')
    op.drop_table('transazioni_interne')
    op.drop_table('transazioni_esterne')
    # ### end Alembic commands ###