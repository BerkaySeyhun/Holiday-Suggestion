# !!!necessary things!!! /latest pip version,latest pil version and latest requests version./

# In this part, we import the necessary libraries for the fields we will use in our codes.

from io import BytesIO  # for use holiday image
import requests as requests  # for use necessary functions
from PIL import Image  # for use holiday image


# Define a class to represent a holiday option
class HolidayOption:
    def __init__(self, name, price, location, duration, activities, image_url):  # attributes
        self.name = name  # holiday name
        self.price = price  # holiday price
        self.location = location  # holiday location
        self.duration = duration  # holiday location (day)
        self.activities = activities  # holidays activities
        self.image_url = image_url  # holiday image


# Create some instances of the HolidayOption class to represent different holiday options
option1 = HolidayOption("Beach Holiday in Antalya", 10000, "antalya", 7, ["swimming", "snorkeling", "sunbathing"],
                        "https://images.pexels.com/photos/2034335/pexels-photo-2034335.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1.jpg")
option2 = HolidayOption("Ski Holiday in Erzurum", 8000, "erzurum", 5, ["skiing", "snowboarding", "hiking"],
                        "https://images.pexels.com/photos/286581/pexels-photo-286581.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1.jpg")
option3 = HolidayOption("City Tour in Istanbul", 6000, "istanbul", 3, ["sightseeing", "shopping", "street Food"],
                        "https://images.pexels.com/photos/3999943/pexels-photo-3999943.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1.jpg")
option4 = HolidayOption("Historical Trip in Izmır", 7000, "izmir", 4, ["cultural", "museum", "sea Food"],
                        "https://images.pexels.com/photos/7524306/pexels-photo-7524306.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1.jpg")
option5 = HolidayOption("Museum Tour in Cappadocia", 5000, "cappadocia", 2, ["balloon", "museum", "cultural Food"],
                        "https://images.pexels.com/photos/2563680/pexels-photo-2563680.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1.jpg")

# Create a list of all the holiday options
options = [option1, option2, option3, option4, option5]  # add all options to our holiday options

# List of holiday destinations and their corresponding activities
destinations = {
    'beach': ['antalya', 'istanbul', 'izmir'],
    'hiking': ['erzurum', 'cappadocia'],
    'city break': ['istanbul', 'izmir'],
    'skiing': ['erzurum'],
    'relaxation': ['izmir', 'cappadocia']
}


# Function to suggest a holiday destination based on a user's favorite activity
def suggest_holiday(favorite_activity):
    # List to store possible holiday suggestions
    suggestions = []

    # Iterate over the keys and values in the destinations dictionary
    for activities, dests in destinations.items():
        # Check if the user's favorite activity is in the list of activities for the destination
        if favorite_activity in activities:
            # If it is, add the destination to the list of suggestions
            suggestions.extend(dests)

    # Check if the list of suggestions is empty
    if len(suggestions) == 0:
        print("Sorry, we don't have any holiday suggestions for your favorite activity.")
    else:
        print("How about a holiday in one of these destinations for some " + favorite_activity + ":")
        print(', '.join(suggestions))

# function that collects user input to a txt file until user writes done
def collect_inputs(filename):
  # Open the file for writing
  with open(filename, 'w') as f:
    # Continuously get user input until they enter 'done'
    while True:
      user_input = input("Enter a line of text (enter 'done' to quit): ")
      if user_input == 'done':
        break
      # Write the user input to the file
      f.write(user_input + '\n')
  print("Inputs collected and written to file successfully!")



# Prompt the user for their budget and desired location
print("-<Holiday Location>-  -Price-")
print("     antalya             10000")
print("     erzurum             8000")
print("     istanbul            6000")
print("     izmir               7000")
print("     cappadocia          5000")
print()  # for a blank line

print("-<Activities>-") # holiday activities
print("beach", "hiking",  "city break",  "skiing", "relaxation")
print()  # for a blank line

budget = int(input("Enter your budget for holiday: "))  # taking user budget for tell options
desired_location = input("Enter your desired location: ")  # taking user desired locations
fav_activity = input("Enter your favorite activity: ")  # taking user desired activity
suggest_holiday(fav_activity) # suggest holiday options for activity

# Iterate through the options and check if they meet the user's specifications
available_options = []
# In the option section, it is the place where all of them are compared by looking at the values received from the user.
for option in options:
    if option.price <= budget and option.location == desired_location:
        available_options.append(option)

# If no options are available, suggest some new options
if not available_options:
    print("Sorry, we don't have any options that meet your specifications.")
    print("Here are some suggestions based on your budget and location:")
    if budget >= 5000:
        print("- Cultural trip in historical location (Price is 7000)")
    if budget >= 8000:
        print("- Ski trip to a mountain resort (Price is 8000)")
    if budget >= 10000:
        print("- Good week in seaside Hotel (Price is 10000)")
else:
    # Print out the available options and allow the user to view the images
    print("Here are the available options:")
    for option in available_options:
        print(f"{option.name} - {option.price}")
        print("Would you like to view a picture of the destination? (y/n)")
        view_picture = input()
        if view_picture == "y":
            # Download the image and open it using PIL
            response = requests.get(
                option.image_url)  # gets the picture of the requested holiday from within its properties
            image = Image.open(BytesIO(response.content))
            image.show()  # shows the holiday image

collect_inputs('inputs.txt') # collects user inputs until the user write done to terminal