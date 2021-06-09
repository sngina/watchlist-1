from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_movies,get_movie,search_movie
from .forms import ReviewForm
from ..models import Review
from flask_login import login_required



# Views

@main.route('/')
def index():
  title = 'Home - Welcome to the Best Movir Review Website Online'
  popular_movies = get_movies('popular')
  upcoming_movie = get_movies('upcoming')
  now_showing = get_movies('now_playing')

  search_movie = request.args.get('movie_query') # gets qury from html with name movie_query

  if search_movie:
    # redirect directs us to another view function 
    # url_for 1st para goes to view function 2nd para moive name is the search_movie(from input)
    return redirect(url_for('.search', movie_name = search_movie))
  else:
    return render_template('index.html', title=title, popular = popular_movies, upcoming = upcoming_movie, now_showing = now_showing)

@main.route('/movie/<int:id>')
@login_required
def movie(id):

  movie = get_movie(id)

  title = f'{movie.title}'

  reviews = Review.get_reviews(movie.id)

  return render_template('movie.html', title = title, movie = movie, reviews = reviews)

@main.route('/search/<movie_name>')
def search(movie_name):
  movie_name_list = movie_name.split(' ') # split muliptle words
  movie_name_format = '+'.join(movie_name_list) # join them with +
  searched_movies = search_movie(movie_name_format)
  title = f'search results for {movie_name}'

  return render_template('search.html', movies = searched_movies)

@main.route('/movie/review/new/<int:id>', methods = ['GET', 'POST'])
def new_review(id):

  form = ReviewForm()
  movie = get_movie(id)

  if form.validate_on_submit():
    title = form.title.data 
    review = form.review.data

    new_review = Review(movie.id, title, movie.poster, review)
    new_review.save_review()
    return redirect(url_for('.movie', id = movie.id))

  title = f'{movie.title} review'
  return render_template('new_review.html', title = title, review_form = form, movie = movie)




