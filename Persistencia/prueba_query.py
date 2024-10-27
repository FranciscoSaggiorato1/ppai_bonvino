from Entidades.vino import Vino
from database_config import session

res = session.query(Vino).all()


# print(res)

for r in res:
    print(r)


