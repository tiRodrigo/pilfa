"""empty message

Revision ID: b80e01ba0eb7
Revises: 74d5ce49db24
Create Date: 2024-05-20 20:23:49.845941

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'b80e01ba0eb7'
down_revision = '74d5ce49db24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipamento',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('equipamento', sa.String(length=200), nullable=True),
    sa.Column('marca', sa.String(length=200), nullable=True),
    sa.Column('quantidade', sa.Integer(), nullable=True),
    sa.Column('acessorios', sa.String(length=200), nullable=True),
    sa.Column('observacoes', sa.String(length=200), nullable=True),
    sa.Column('fk_nivel_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fk_nivel_id'], ['nivel.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('equipmento')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('equipmento',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('equipamento', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('marca', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('quantidade', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('acessorios', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('observacoes', mysql.VARCHAR(length=200), nullable=True),
    sa.Column('fk_nivel_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['fk_nivel_id'], ['nivel.id'], name='equipmento_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('equipamento')
    # ### end Alembic commands ###
