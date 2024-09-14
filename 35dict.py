datas = {'nepal': 'Kathamandu','india': 'New Delhi', 'us': 'WDC'}

datas['nepal'] = 'Ktm'
datas['japan'] = 'Tokyo'



print(f"Capital city of Nepal is {datas['nepal']}")
print(f"Capital city of Japan is {datas['japan']}")


person_info = {
    'name': 'Bishworaj Poudel',
    'age': 27,
    'fav_movies': ['3 Idiots', 'Godfather','Social Network']
}

print(person_info['fav_movies'][0])

print('name' in person_info)

for key in person_info:
    print(f"key is {key} and value is {person_info[key]}")


fav_movies = {
    'Godfather': 2000,
    'ABC': 2024
}

fav_movies['xyz'] = 2024
fav_movies['ABC'] = 2001

fav_movies.pop('ABC')
print(fav_movies)


