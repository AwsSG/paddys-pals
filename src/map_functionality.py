import folium

def generate_map():

    #Dublin, could change this to users location though?
    start_coords = (53.350140, -6.266155)

    main_map = folium.Map(
            location = start_coords,
            zoom_start = 14,
            width = '100%',
            height = '100%'
            )

    main_map.save('src/templates/map.html')
