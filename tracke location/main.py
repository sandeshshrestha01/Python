import phonenumbers
import folium
from myphone import number
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode

# Parse the phone number
pepnenumber = phonenumbers.parse(number, "NP")  # Replace "NP" with the appropriate region code for Nepal

# Get the location
location = geocoder.description_for_number(pepnenumber, "en")
print(f"Location: {location}")

# Get the carrier
service_provider = carrier.name_for_number(pepnenumber, "en")
print(f"Service Provider: {service_provider}")

# Use OpenCage Geocoder for detailed location
key = 'd807c26437f94f6d8785428d0b9c03a3'
geocoder = OpenCageGeocode(key)

# Query OpenCage with the location description
query = str(location)
results = geocoder.geocode(query)

if results:
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Latitude: {lat}, Longitude: {lng}")

    # Create a map centered at the location
    myMap = folium.Map(location=[lat, lng], zoom_start=15)
    folium.Marker([lat, lng], popup=location).add_to(myMap)

    # Save the map to an HTML file
    myMap.save("mylocation.html")
    print("Map has been saved as 'mylocation.html'.")
else:
    print("No results found for the location.")
