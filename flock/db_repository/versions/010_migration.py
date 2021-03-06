from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
value = Table('value', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
)

rating = Table('rating', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('company_id', Integer),
    Column('user_id', Integer),
    Column('value_id', Integer),
    Column('rating', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['value'].create()
    post_meta.tables['rating'].columns['value_id'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['value'].drop()
    post_meta.tables['rating'].columns['value_id'].drop()
