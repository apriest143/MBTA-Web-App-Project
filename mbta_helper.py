import json
import os
import pprint
import urllib.request

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API keys from environment variables
MAPBOX_TOKEN = os.getenv("MAPBOX_TOKEN")
MBTA_API_KEY = os.getenv("MBTA_API_KEY")

# Useful base URLs (you need to add the appropriate parameters for each API request)
MAPBOX_BASE_URL = "https://api.mapbox.com/geocoding/v5/mapbox.places"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"


# A little bit of scaffolding if you want to use it
def get_json(url: str) -> dict:
    """
    Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

    Both get_lat_lng() and get_nearest_station() might need to use this function.
    """
    pass




def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    
    query = place_name.replace(" ", "%20") # In URL encoding, spaces are typically replaced with "%20". You can also use `urllib.parse.quote` function. 
    url=f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    print(url) # Try this URL in your browser first

    with urllib.request.urlopen(url) as resp:
        response_text = resp.read().decode("utf-8")
        response_data = json.loads(response_text)
       # pprint.pprint(response_data)
        points = response_data['features'][0]['geometry']['coordinates']
        print(points)
        latitude = points[0]
        longitude = points[1]
        print(longitude)
    return (latitude, longitude)


def get_nearest_station(latitude: str, longitude: str) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    query = f"/data/{latitude}/attributes/latitude/data/{longitude}/attributes/longitude"
    url=f"{MBTA_BASE_URL}/{query}.json?access_token={MBTA_API_KEY}&types=poi"
    print(url) # Try this URL in your browser first

    with urllib.request.urlopen(url) as resp:
        response_text = resp.read().decode("utf-8")
        response_data = json.loads(response_text)
        pprint.pprint(response_data)
        points = response_data['features'][0]['geometry']['coordinates']
       # print(points)
       
    pass


def find_stop_near(place_name: str) -> tuple[str, bool]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    pass


def main():
    """
    You should test all the above functions here
    """
    place_name = input("Enter the name of your place:")
    get_nearest_station(get_lat_lng(place_name))
    pass


if __name__ == "__main__":
    main()
