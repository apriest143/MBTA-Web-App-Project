from flask import Flask
from flask import request
from flask import render_template
from mbta_helper import find_stop_near
from markupsafe import escape


app = Flask(__name__)

#This route is the one that is opened upon running the flask. It will prompt the user to input their location into
#a form and push that data into the /nearest_mbta page using the post method.
@app.route("/")
def index():
    return '''
    <!doctype html>
    <html>
        <head>
            <title>Find Nearest MBTA Station</title>
        </head>
        <body>
            <h1> Hello! Enter a location to find the Nearest MBTA station.</h1>
            <form action = "/nearest_mbta" method = "post">
                <label for = "place"> Place name:</label>
                <input type = "text" id = "place" name =  "place" required>
                <input type = "submit" value = "Submit">
            </form>
        </body>
    </html>
    '''

#This function grabs the location submitted by the user in the previous webpage. It stores this name as place_name.
#it then runs the find_nearest_mbta function using place_name and stores the location that function returns as result
#It then checks to see if the output is correct. If there are any errors it will prompt the user to return to the beginning
@app.route('/nearest_mbta', methods=['POST'])
def nearest_mbta():
    place_name = request.form.get('place_name')  # Get the place name from form data
    
    # Use the helper function to call the find_stop_near function and store the output as result
    result = find_stop_near(place_name)
    
    if result:
        station_name, accessibility = result['station_name'], result['accessible']
        return render_template('index.html', station=station_name, accessible=accessibility)
    else:
        # Render an error page if something went wrong
        return '''
        <!doctype html>
        <html>
            <head><title>Error</title></head>
            <body>
                <h1>Error: Unable to find station</h1>
                <p>We couldn't find a station for the place you entered. Please try again.</p>
                <a href="/">Go back to the home page</a>
            </body>
        </html>
        '''



if __name__ == "__main__":
    app.run(debug=True)
