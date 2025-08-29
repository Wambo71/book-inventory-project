"""Recreates customers and books table saely

Revision ID: ab6132f55fad
Revises: d49a25c53bc2
Create Date: 2025-08-29 15:59:17.309304

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ab6132f55fad'
down_revision: Union[str, None] = 'd49a25c53bc2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "customers_new",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String, nullable=False),
        sa.Column("email", sa.String, nullable=False, unique=True),
        sa.Column("address", sa.String, nullable=False),
    )

    conn = op.get_bind()
    conn.execute(sa.text("""
        INSERT INTO customers_new (id, name, email, address)
        SELECT MIN(id), name, email, address
        FROM customers
        GROUP BY name, email, address
    """))

    op.drop_table("customers")
    op.rename_table("customers_new", "customers")

    # --- Recreate books ---
    op.create_table(
        "books_new",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("author", sa.String, nullable=False),
        sa.Column("price", sa.Float, nullable=False),
        sa.Column("stock", sa.Integer, nullable=False),
    )

    conn.execute(sa.text("""
        INSERT INTO books_new (id, title, author, price, stock)
        SELECT id, title, author, price, stock
        FROM books
    """))

    op.drop_table("books")
    op.rename_table("books_new", "books")





def downgrade() -> None:
    op.create_table(
        "customers_old",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String),
        sa.Column("email", sa.String),
        sa.Column("address", sa.String),
    )

    conn = op.get_bind()
    conn.execute(sa.text("""
        INSERT INTO customers_old (id, name, email, address)
        SELECT id, name, email, address FROM customers
    """))

    op.drop_table("customers")
    op.rename_table("customers_old", "customers")

    # --- Downgrade books ---
    op.create_table(
        "books_old",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String),
        sa.Column("author", sa.String),
        sa.Column("price", sa.Float),
        sa.Column("stock", sa.Integer),
    )

    conn.execute(sa.text("""
        INSERT INTO books_old (id, title, author, price, stock)
        SELECT id, title, author, price, stock FROM books
    """))

    op.drop_table("books")
    op.rename_table("books_old", "books")

