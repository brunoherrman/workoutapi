"""'add_centro_treinamento'

Revision ID: 4b327f1c77b7
Revises: 2eff3a6b80f2
Create Date: 2024-07-08 15:26:06.844405

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4b327f1c77b7'
down_revision: Union[str, None] = '2eff3a6b80f2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('centro_treinamento',
    sa.Column('pk_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('endereco', sa.String(length=100), nullable=False),
    sa.Column('telefone', sa.String(length=20), nullable=False),
    sa.Column('id', sa.UUID(), nullable=False),
    sa.PrimaryKeyConstraint('pk_id')
    )
    op.add_column('atletas', sa.Column('centro_treinamento_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'atletas', 'centro_treinamento', ['centro_treinamento_id'], ['pk_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'atletas', type_='foreignkey')
    op.drop_column('atletas', 'centro_treinamento_id')
    op.drop_table('centro_treinamento')
    # ### end Alembic commands ###