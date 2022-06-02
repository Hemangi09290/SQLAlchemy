from main import User,engine,Base


Base.metadata.create_all(engine)

'''
>>> python create_db.py
<User username=JOnathan email=jona@jona.com>
2022-06-02 17:06:16,354 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-06-02 17:06:16,354 INFO sqlalchemy.engine.Engine PRAGMA main.table_info("users")
2022-06-02 17:06:16,354 INFO sqlalchemy.engine.Engine [raw sql] ()
2022-06-02 17:06:16,357 INFO sqlalchemy.engine.Engine COMMIT
PS C:\Users\Akshay Barve\Downloads\Introduction-to-SQLAlchemy-main>
'''