from sqlalchemy import MetaData, Table, Column, String, Integer, create_engine, ForeignKey

meta = MetaData()

authors = Table("lol&", meta,
                Column('id_game', Integer, primary_key=True),
                Column('name', String(255), nullable=False),
                Column('comp_id',String(255)),
                Column('rock', Integer),
                Column('name', Integer),
                Column('name', Integer)
                )

engine = create_engine("mysql+mysqlconnector://root:root@localhost/RPS", echo=True)
meta.create_all(engine)

conn = engine.connect()

add_author_query = authors.insert().values(name='Lutz')
conn.execute(add_author_query)

add_book_query = books.insert().values(title='learn Py',
                                       id_author=1,
                                       genre='Education',
                                       price=1299)
conn.execute(add_book_query)
add_book_query_sec = books.insert().values(title='Clear Py',
                                           id_author=1,
                                           genre='Education',
                                           price=956)
conn.execute(add_book_query_sec)
