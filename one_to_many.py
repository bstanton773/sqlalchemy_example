from sqlalchemy import Column, Integer, String, DateTime, func, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(25))
    password = Column(String(25))
    first_name = Column(String(25))
    last_name = Column(String(25))
    posts = relationship('Post', back_populates='author', uselist=True)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.password = kwargs['password'][::-2]

    def __repr__(self):
        return f"<User {self.id}|{self.username}>"
    
    def check_password(self, password_guess):
        return self.password == password_guess[::-2]
    

class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    date_created = Column(DateTime, default=func.now())
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    author = relationship('User', back_populates='posts')

    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"
    


from sqlalchemy import create_engine

engine = create_engine('sqlite:///example1.db', echo=True)

Session = sessionmaker(engine)

if __name__ == "__main__":
    with Session() as session:
        Base.metadata.create_all(engine)
    
