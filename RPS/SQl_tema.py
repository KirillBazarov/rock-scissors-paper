from sqlalchemy import MetaData, Table, Column, String, Integer, create_engine, ForeignKey
from RPS import pc_data, players_data

meta = MetaData()

statistics = Table("stats", meta,
                   Column('id_game', Integer, primary_key=True),
                   Column('name', String(255), nullable=False),
                   Column('player_choice', Integer),
                   Column('computer_choice', Integer)
                   )

engine = create_engine("mysql+mysqlconnector://root:root@localhost/RPS", echo=True)
meta.create_all(engine)

conn = engine.connect()

add_game_data = statistics.insert().values(name=players_data.name, player_choice=players_data.vibor_igroka,
                                           computer_choice=pc_data.vibor_pc, )
conn.execute(add_game_data)
