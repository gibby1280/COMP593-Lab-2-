def main():

    # TODO: Step 2 - Create a complex data structure
    about_me = {
        'full_name' : 'Gibson Davidson',
        'student_id' : '10279444',
        'pizza_toppings' : [
            'BACON',
            'HAM',
            'PINEAPPLE',
        ],
        'movies' :[
            {
               'favourite movie' : 'No Country For Old Men',
               'genre' : 'thriller',
               'title' : 'No Country For Old Men',   
            },
            {
                "Second favourite moveie" : 'Baby Driver',
                'genre' : 'action',
                'title' : 'Baby Driver',
            },
        ]

    }
 # TODO: Step 3 - Add another movie to the data structure
    third_favourite_movie = {
        'title' : 'Bullet Train',
        'genre' : 'action',
    }
    about_me ['movies'].append(third_favourite_movie)
    
# TODO: Step 4 - Function that prints student name and ID	
def print_student_name_and_id(about_me):
    
    full_name = about_me['full_name']
    student_id = about_me['student_id']

    print(f' My name is {full_name} but you can call me Sir {full_name}. My student id is {student_id}')
    for a in about_me['full_name', 'student_id']:
        return print_student_name_and_id
    
    
# TODO: Step 5 - Function that adds pizza toppings to data structure
def add_pizza_toppings(about_me, toppings):
    about_me['toppings'].extend()
    'toppings' : [

    ]


    return

# TODO: Step 6 - Function that prints bullet list of pizza toppings
def print_pizza_toppings(about_me):
    print('my favourite pizza toppings are:')
    for pizza_toppings in about_me:

    return

# TODO: Step 7 - Function that prints comma-separated list of movie genres
def print_movie_genres(about_me):
    genre_list = [movie["genre"] for movie in about_me]
    genres = ", ".join(genre_list)
    if len(genre_list) > 1:
        genres = genres.rsplit(", ", 1)[0] + " and " + genre_list[-1]
    print(f"I like to watch {genres} movies.")

def main():
    movies = [{"genre": "Action"}, {"genre": "Comedy"}, {"genre": "Drama"}]
    print_movie_genres(movies)

    return 

# TODO: Step 8 - Function that prints comma-separated list of movie titles
def print_movie_titles(movie_list):
    title_list = [movie["title"].title() for movie in about_me]
    titles = ", ".join(title_list)
    if len(title_list) > 1:
        titles = titles.rsplit(", ", 1)[0] + " and " + title_list[-1]
    print(f"Some of my favorite movies are {titles}!")

def main():
    movies = [{"title": "Baby Driver"}, {"title": "Bullet Train"}, {"title": "No Countro For Old Men"}]
    print_movie_titles(movies)

    return
    
if __name__ == '__main__':
    main()