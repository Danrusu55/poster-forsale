# Import from peewee
from peewee import *

# Connect to the SQLite database
db = SqliteDatabase('forsaledb.db')

# Define what a 'School' is
class Campaign(Model):
  name = CharField()
  title1 = CharField()
  title2 = CharField()
  title3 = CharField()
  title4 = CharField()
  title5 = CharField()
  body = CharField()
  licloc = CharField()
  image = CharField()
  login = CharField()
  password = CharField()

  class Meta:
    database = db

class City(Model):
  campaign = ForeignKeyField(Campaign, related_name='cities')
  mainurl = CharField()
  city = CharField()
  phone = CharField()
  lastposted = DateField()
  daystowait = IntegerField()

  class Meta:
    database = db
