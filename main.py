from sqlalchemy.orm import declarative_base,sessionmaker
from sqlalchemy import Column,String,DateTime,Integer,create_engine
from datetime import datetime
import os

BASE_DIR=os.path.dirname(os.path.realpath(__file__))

connection_string="sqlite:///"+os.path.join(BASE_DIR,'site.db')


Base=declarative_base()

engine=create_engine(connection_string,echo=True)

Session=sessionmaker()

""""
class User
    id int
    username str
    email str
    date_created datetime

"""

class User(Base):
    __tablename__='users'
    id=Column(Integer(),primary_key=True)
    username=Column(String(25),nullable=False,unique=True)
    email=Column(String(80),unique=True,nullable=False)
    date_created=Column(DateTime(),default=datetime.utcnow)

    def __repr__(self):
        return f"<User username={self.username} email={self.email}>"


new_user=User(id=1,username="JOnathan",email="jona@jona.com")
print(new_user)

'''
python
Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from main import User
<User username=JOnathan email=jona@jona.com>
>>> User
<class 'main.User'>
>>> User__tablename__
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'User__tablename__' is not defined
>>> User.__tablename__
'users'
>>> User.__table__
Table('users', MetaData(), Column('id', Integer(), table=<users>, primary_key=True, nullable=False), Column('username', String(length=25), table=<users>, nullable=False), Column('email', String(length=80), table=<users>, nullable=False), Column('date_created', DateTime(), table=<users>, default=ColumnDefault(<function datetime.utcnow at 0x0000024863F95A60>)), schema=None)
'''
