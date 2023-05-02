from datetime import datetime
from sql.database import db_metadata, db_engine, Base
from sqlalchemy import Table, Column, String, Integer, DateTime

payment = Table(
    "payment",
    db_metadata,
    Column("payment_id", Integer, primary_key=True, autoincrement=True),
    Column("reg_date", DateTime(timezone=True), nullable=False, default=datetime.now),
    Column("value", Integer)
)

payment.metadata.create_all(db_engine)