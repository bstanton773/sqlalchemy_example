from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import DeclarativeBase, relationship, sessionmaker

class Base(DeclarativeBase):
    pass


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    body = Column(String)
    categories = relationship('Category', secondary='post_category', backref='posts', uselist=True)

    def __repr__(self):
        return f"<Post {self.id}|{self.title}>"

class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True)
    category_name = Column(String(50))
    description = Column(String(100))

    def __repr__(self):
        return f"<Category {self.id}|{self.category_name}>"


class PostCategory(Base):
    __tablename__ = "post_category"
    post_id = Column(Integer, ForeignKey('post.id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('category.id'), primary_key=True)


from sqlalchemy import create_engine

engine = create_engine('sqlite:///example2.db', echo=True)

Session = sessionmaker(engine)

if __name__ == "__main__":
    with Session() as session:
        Base.metadata.create_all(engine)
    