from main import User,Session,engine


local_session=Session(bind=engine)


#returns first 3 user name objects
# users=local_session.query(User).all()[:3]
# for user in users:
#     print(user.username)


#query for one object

jona=local_session.query(User).filter(User.username=="jona").first()

print(jona)


'''
PS C:\Users\Akshay Barve\Downloads\Introduction-to-SQLAlchemy-main> python retrieving.py
<User username=JOnathan email=jona@jona.com>
2022-06-02 18:09:13,348 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2022-06-02 18:09:13,350 INFO sqlalchemy.engine.Engine SELECT users.id AS users_id, users.username AS users_username, users.email AS users_email, users.date_created AS users_date_created
FROM users
WHERE users.username = ?
 LIMIT ? OFFSET ?
2022-06-02 18:09:13,351 INFO sqlalchemy.engine.Engine [generated in 0.00088s] ('jona', 1, 0)
None
PS C:\Users\Akshay Barve\Downloads\Introduction-to-SQLAlchemy-main> 
'''

