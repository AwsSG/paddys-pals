import folium
from sys import stderr
from .database import mongo
from .party import Party

def create_party_from_cursor(cursor):
    """ Populate a party object with data from a mongodb cursor """
    if cursor:
        party = Party(cursor['_id'], cursor['longitude'], cursor['latitude'],
            cursor['start_time'],cursor['end_time'], cursor['video_link'],cursor['party_password'], cursor['description'],cursor['name'])

        return party

def get_parties():
    """ Create a party object for each database record """
    parties_info = mongo.db.parties.find()
    parties = list(map(create_party_from_cursor, parties_info))
    return parties


def generate_map():
    """ Generate and save the map to map.html """
    #Dublin, could change this to users location though?
    start_coords = (53.350140, -6.266155)

    main_map = folium.Map(
            location = start_coords,
            zoom_start = 1,
            width = '100%',
            height = '100%'
            )

    #Add a marker for each party stored in the database
    parties = get_parties()
    for party in parties:
        popup_content = folium.Html(f'''<b> {party.name} <p> \
                <b> Start: </b>{party.start_time} </p> \
                <b> End: </b>{party.end_time} </p> \
                <p> {party.description}</p> \
                <a href="{party.video_link}">Join here</a>''',script=True)
        popup = folium.Popup(popup_content, max_width=2650)
        folium.Marker(
                location = [party.latitude, party.longitude],
                popup = popup
                ).add_to(main_map)

    main_map.save('src/templates/map.html')
