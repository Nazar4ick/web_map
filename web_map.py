import folium
import googlemaps


def read_file(path, year, country):
    '''
    reads the file with the locations
    :param path: str
    :param year: int
    :param country: str
    :return: set
    '''
    locations = []
    f = open(path, mode='r')
    for line in f.readlines():
        line = line.strip().split('\t')
        # remove all white spaces
        while '' in line:
            line.remove('')
        # filter all films with the specified year
        if line[0].split('(')[1][0:4] == str(year):
            # add location
            if line[-1][0] != '(':
                locations.append(line[-1])
            else:
                locations.append(line[-2])
    # filter only those films which are filmed the same country
    country_locations = []
    for element in locations:
        if element.split(', ')[-1] == country:
            country_locations.append(element)
    return set(country_locations)


def get_coordinates(locs, coords):
    '''
    returns 10 closest film locations
    :param locs: set
    :param coords: tuple
    :return: list
    '''
    maps = googlemaps.Client(key='AIzaSyAd3skpeldG352OyzjvBwzj_7p0AzUFB-k')
    locs = list(locs)
    for i in range(len(locs)):
        location = maps.geocode(locs[i])
        try:
            f_coords = (location[0]['geometry']['location']['lat'],
                        location[0]['geometry']['location']['lng'])
            # measure distance in degrees
            distance = ((coords[0] - f_coords[0])**2 +
                        (coords[1] - f_coords[1])**2)**0.5
            locs[i] = (f_coords, distance, locs[i])
        except IndexError:
            pass
    for place in locs:
        if type(place[1]) == str:
            locs.remove(place)
    locs.sort(key=lambda x: x[1])
    # return first 10 locations, if there are more then 10 in the list
    if len(locs) > 10:
        return locs[0:10]
    return locs


def create_map(loc, year):
    '''
    creates a map with 10 closest film locations
    :param loc: tuple
    :param year: int
    :return: None
    '''
    country = get_country(loc)
    locations = read_file('locations.list', year, country)
    distances = get_coordinates(locations, loc)
    mapa = folium.Map(location=list(loc), zoom_start=10)
    film_map = folium.FeatureGroup(name='films')
    for place in distances:
        film_map.add_child(folium.Marker(location=list(place[0]),
                                         popup='Тут знімався фільм',
                                         icon=folium.Icon()))
    dist_len = folium.FeatureGroup(name='distance')
    # add distance as a layer
    # note: each degree is 111,000 metres
    for dist in distances:
        dist_len.add_child(folium.Marker(location=list(dist[0]),
                                         popup=str(round(dist[1]*111, 2))+' km',
                                         icon=folium.Icon()))
    film_map.add_child(folium.Marker(location=list(loc), popup='You are here',
                                     icon=folium.Icon(color='red')))

    mapa.add_child(film_map)
    mapa.add_child(dist_len)
    mapa.add_child(folium.LayerControl())
    mapa.save('Films.html')


def get_country(loc):
    '''
    gets the country by coordinates
    :param loc: tuple
    :return: srt
    >>> get_country((50.4500336, 30.5241361))
    'Ukraine'
    '''
    maps = googlemaps.Client(key='AIzaSyAbj08RLqlA6urGvGaFFB84DdDcPa1a5c4')
    country = maps.reverse_geocode(loc)[0]['formatted_address'].split(', ')
    if country[-1].isdigit():
        return country[-2]
    return country[-1]


create_map((50.4500336, 30.5241361), 2006)
