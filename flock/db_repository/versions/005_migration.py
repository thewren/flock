from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=64)),
    Column('password', String(length=64)),
    Column('role', SmallInteger, default=ColumnDefault(0)),
    Column('about_me', String(length=140)),
    Column('last_seen', DateTime),
    Column('age', Integer),
    Column('gender', String(length=64)),
    Column('location', String(length=64)),
    Column('zip_code', String(length=15)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['location'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['user'].columns['location'].drop()
