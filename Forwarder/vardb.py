from sqlalchemy import Column, String
from Forwarder import DB_URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session


def start() -> scoped_session:
    engine = create_engine(DB_URL)
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


try:
    BASE = declarative_base()
    SESSION = start()
except AttributeError as e:
    print("DB_URI is not configured. Features depending on the database might have issues.")
    print(str(e))


class dbvars(BASE):
    __tablename__ = "dbvariables"
    name = Column(String(14), primary_key=True)
    value = Column(String(50))

    def __init__(self, name, value):
        self.name = name
        self.value = value


dbvars.__table__.create(checkfirst=True)


def add_variable(name,value):
    __var = dbvars(str(name),str(value))
    SESSION.add(__var)
    SESSION.commit()


def del_variable(name):
    var = SESSION.query(dbvars).get(str(name))
    SESSION.delete(var)
    SESSION.commit()


def get_all_variables():
    vars = SESSION.query(dbvars).all()
    SESSION.close()
    return vars


def find_variable(name):
    try:
        return SESSION.query(dbvars).filter(
            dbvars.name == str(name)).one()
    except BaseException:
        return None
    finally:
        SESSION.close()


def get_variable(name):
    var = SESSION.query(dbvars).filter(dbvars.name == str(name)).one()
    return var.value

def edit_variable(name,value):
    SESSION.query(dbvars).filter(dbvars.name == str(name)).update({dbvars.value: value})
    SESSION.commit()
