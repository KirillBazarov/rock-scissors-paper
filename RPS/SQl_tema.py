from sqlalchemy import MetaData, Table, Column, String, Integer, create_engine, ForeignKey
# import RPS.py


meta = MetaData()

statistics = Table("lol&", meta,
                   Column('id_game', Integer, primary_key=True),
                   Column('name', String(255), nullable=False),
                   # Column('comp_id', String(255)),
                   Column('player_choice', Integer),
                   Column('computer_choice', Integer)
                   )

engine = create_engine("mysql+mysqlconnector://root:root@localhost/RPS", echo=True)
meta.create_all(engine)

conn = engine.connect()

add_game_data = statistics.insert().values()
conn.execute(add_game_data)