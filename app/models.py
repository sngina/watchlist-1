# from enum import unique
# from app.main.views import index
from sqlalchemy.orm import backref
from . import db 
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime


class User( UserMixin,db.Model): # for creating new user
  __tablename__ = 'users' # allows us to give table in db a proper name

  id = db.Column(db.Integer, primary_key = True) # rep a single column 1st para type of data to be stored
  username = db.Column(db.String(255), index = True) # db.String type of data to be stored is string (255) is max number
  email = db.Column(db.String(255), unique = True, index = True)
  role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  password_secure = db.Column(db.String(255))

  reviews = db.relationship('Review',backref = 'user' , lazy = 'dynamic')
  def __repr__(self):
    return f'User {self.username}' # not important just for debuging
  username
  pass_secure = db.Column(db.String(255))
  @property 
  def password(self):
      raise AttributeError('You cannot read the password attribute')
  
  @password.setter
  def password(self, password):
      self.pass_secure = generate_password_hash(password)

  def verify_password(self,password):
      return check_password_hash(self.pass_secure,password)



  #connect the users access with the users with the User...
class Role(db.Model):
  __tablename__ = 'roles'

  id = db.Column(db.Integer, primary_key = True)
  name = db.Column(db.String(255))
  users = db.relationship('User', backref = 'role', lazy="dynamic")
    # creates virtual column that will connect with foregin key
      # 1st > class referencing 
      # 2nd > allow us to access and set our user class (get the role of user instance we can just run)
      # 3rd > our objects will be loaded on access and filtered before returning

  def __repr__(self):
    return f'User {self.name}'

class Movie:
  def __init__(self,id,title,overview,poster,vote_average,vote_count):
    self.id =id
    self.title = title
    self.overview = overview
    self.poster = 'https://image.tmdb.org/t/p/w500'+ poster
    self.vote_average = vote_average
    self.vote_count = vote_count

class Review (db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    movie_id = db.Column(db.Integer)
    movie_title = db.Column(db.String)
    image_path = db.Column(db.String)
    movie_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    def save_review(self):
      db.session.add(self)
      db.session.commit()

    @classmethod
    def clear_reviews(cls):
      Review.all_reviews.clear()

    @classmethod
    def get_reviews(cls, id):
      reviews = Review.query.filter_by(movie_id =id).all()

      return reviews
    # function that retrieves a user when a unique identifier is passed..
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
