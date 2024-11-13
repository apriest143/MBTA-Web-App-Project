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


# # A little bit of scaffolding if you want to use it
# def get_json(url: str) -> dict:
#     """
#     Given a properly formatted URL for a JSON web API request, return a Python JSON object containing the response to that request.

#     Both get_lat_lng() and get_nearest_station() might need to use this function.
#     """
#     pass




def get_lat_lng(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return a (latitude, longitude) tuple with the coordinates of the given place.

    See https://docs.mapbox.com/api/search/geocoding/ for Mapbox Geocoding API URL formatting requirements.
    """
    
    query = place_name.replace(" ", "%20") # In URL encoding, spaces are typically replaced with "%20". You can also use `urllib.parse.quote` function. 
    url=f"{MAPBOX_BASE_URL}/{query}.json?access_token={MAPBOX_TOKEN}&types=poi"
    print(url) # Try this URL in your browser first

    try:
        with urllib.request.urlopen(url) as resp:
            response_text = resp.read().decode("utf-8")
            response_data = json.loads(response_text)
        # pprint.pprint(response_data)
            points = response_data['features'][0]['geometry']['coordinates']
            print(points)
            # FOR SOME REASON THE POINTS ARE WRONG (LONG GOES BEFORE LAT SHOULD BE INVERSE)

            latitude = points[1]
            longitude = points[0]
            print(latitude, longitude)
        return latitude, longitude


def get_nearest_station(latitude: float, longitude: float) -> tuple[str, bool]:
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible) tuple for the nearest MBTA station to the given coordinates.

    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL formatting requirements for the 'GET /stops' API.
    """
    radius = 100
    query = f"?filter[latitude]={latitude}&filter[longitude]={longitude}&filter[radius]=10"
    url=f"{MBTA_BASE_URL}{query}=access_token={MBTA_API_KEY}"
    print(url) # Try this URL in your browser first'

    with urllib.request.urlopen(url) as resp:
        response_text = resp.read().decode("utf-8")
        response_data = json.loads(response_text)
       # stop = response_data['features'][0]['geometry']['coordinates']
        #pprint.pprint(response_data)
    #   points = response_data['features'][0]['geometry']['coordinates']
       # print(points)b
        if "data" in response_data:
            result  = response_data["data"][0]
            #print (stop)
            station_name = result["attributes"]["name"]
            accessible = result["attributes"]["wheelchair_boarding"]
            if accessible == 1:
                accessible = "has wheelchair boarding"
            if accessible == 0:
                accessible = "does not have wheelchair boarding"
            #print (station)
            #print (wheelchair)
            return station_name, accessible


def find_stop_near(place_name: str) -> tuple[str, str]:
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.

    This function might use all the functions above.
    """
    #place_name = input("Enter the name of your place:")
    latitude, longitude = get_lat_lng(place_name)
    response = get_nearest_station(latitude, longitude)
    print (response)
    return response
    
      #  station_name, accessibility = result['station_name'], result['accessible']


def main():
    """
    You should test all the above functions here
    """
    place_name = input("Enter the name of your place:")
    latitude, longitude = get_lat_lng(place_name)
    response = get_nearest_station(latitude, longitude)
    print (response)
    return response


if __name__ == "__main__":
    main()
