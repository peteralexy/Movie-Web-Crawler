from django.shortcuts import render
from .models import Film, Actor
from .forms import FilmForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Create your views here.
#rendering the index view
def index(request):
    return render(request, 'index.html')
    #films = Film.objects.order_by('film_name')
    #return render(request, 'index.html', {'films': films})
#rendering the film list view
def films(request):
    films = Film.objects.order_by('film_name')
    return render(request, 'films.html', {'films': films})
#rendering the view of a film
def film(request, film_id):
    film = Film.objects.get(id=film_id)
    actors = film.actor_set.order_by('actor_name')
    return render(request, 'film.html', {'film':film ,'actors': actors})
#rendering the view of a new film
def new_film(request):
    if request.method != 'POST':
        form = FilmForm()
    else:
        form = FilmForm(request.POST)
        if form.is_valid():
            #init new movie
            new_movie = Film()
            #give the form value to the name
            new_movie.film_name = form.data['film_name']
            #give the film its name
            movie_name = new_movie.film_name
            #split the words to for the url
            movie_name = movie_name.split()
            #keep these lower case
            smallWords = ['and', 'or', 'the', 'of', 'film']
            card_dict = {}
            #filter certain symbols such as & and '
            for word in movie_name:
                if word not in smallWords:
                    word = word.title()
                if word == '&':
                    word = "%26"
                if word == "'":
                    word = "%27"
            #bs4 settings
            url = "_".join(movie_name)
            movie_url = 'https://en.wikipedia.org/wiki/' + url
            client = urlopen(movie_url)
            page_html = client.read()
            client.close()
            soup = BeautifulSoup(page_html, 'html.parser')
            table = soup.find('table', {'class': 'infobox vevent'})
            #getting the movie url
            if table:
                pass
            else:
                #if the table doesn't exists, since it doesn't have (film) in the url
                my_url = 'https://en.wikipedia.org/wiki/' + url + "_(film)"
                client = urlopen(my_url)
                page_html = client.read()
                client.close()
                soup = BeautifulSoup(page_html, "html.parser")
                table = soup.find('table', {'class': 'infobox vevent'})

            #looping through the table data after the poster
            for row in table.findAll("tr")[2:]:
                role = row.findAll("th")
                values = row.findAll("td")
                for value in values:
                    #pass
                    #print(value.getText())
                    card_dict[role[0].getText()] = value.getText()
            #removing things like [1] [2] that appear at the end of certain attributes
            for key, value in card_dict.items():
                if value[-1] == ']':
                    card_dict[key] = value[:-3]
            #creating an actor array from an actor string
            actor_array = card_dict['Starring'].split('\n')
            #the first and last actors are a null string ''
            #remove them from the array
            actor_array.pop(0)
            actor_array.pop(-1)
            card_dict['Starring'] = actor_array
            #editing the release date to look better
            r_date = card_dict['Release date']
            #format date, remove the comma at the end of the day number and monthd
            new_date = r_date.split()
            if new_date[1][1] == "," and len(new_date[1]) == 2:
                new_date[1] = new_date[1][:1]
            elif new_date[1][2] == ",":
                new_date[1] = new_date[1][:2]
            #date appearance
            last_date = new_date[2] + "-" + new_date[0] + "-" + new_date[1]
            card_dict['Release date'] = last_date
            #runtime
            runtime_1 = card_dict['Running time']
            runtime_2 = runtime_1.split()
            runtime_3 = runtime_2[0]
            card_dict['Running time'] = runtime_3
            #setting the model attributes
            new_movie.director_name = card_dict['Directed by']
            new_movie.movie_runtime = int(card_dict['Running time'])
            new_movie.release_date = card_dict['Release date']
            #getting the poster url
            row = table.findAll('tr')[1]
            image = row.img['src']
            new_movie.movie_poster = image
            new_movie.save()
            #link actors from their array to the movie they play in
            for new_actor in card_dict['Starring']:
                actor = Actor()
                actor.film = new_movie
                actor.actor_name = new_actor
                actor.save()
                
            return HttpResponseRedirect(reverse('movies:index'))
    
    return render(request, 'new_film.html', {'form': form})