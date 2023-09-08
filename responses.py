import requests
from bs4 import BeautifulSoup


def handle_response(message) -> str:

    # Normalize the message to lower case
    p_message = message.lower()

    #  Initialize return message variable
    return_message = ""

    if p_message == 'help':
        return "Type in a Pokemon's ability.\nUsing an exclamation mark before the ability name will result in the response being returned to the current channel.\n" \
                         "Spaces are ok and the command isn't case-sensitive."


    # Add ability to a list
    ability = [p_message]

    # Initialize beautiful soup object
    URL = "https://bulbapedia.bulbagarden.net/wiki/Ability"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib

    # Parse message to get the specific ability name
    ability_table = soup.find('table', attrs={'class': 'roundy'})
    abilities = {}

    # Parse through ability table and extract the ability name and text.
    for row in ability_table.find_all('tr'):
        columns = row.find_all('td')

        if len(columns) >= 2:
            ability_name = columns[1].text.strip()
            ability_text = columns[2].text.strip()

        if ability_name.lower() in ability:
            abilities[ability_name] = ability_text

    for ability_name, ability_text in abilities.items():
        return_message = ability_name.title() + ': ' + ability_text.capitalize() + '\n'

    if not len(abilities):
        return_message = "Ability doesn't exist or is spelt wrong. Please enter in another."

    return return_message


def write_txt():
    p_message = message.lower()

    URL = "https://bulbapedia.bulbagarden.net/wiki/Ability"
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html5lib')  # If this line causes an error, run 'pip install html5lib' or install html5lib

    ability_table = soup.find('table', attrs={'class': 'roundy'})
    abilities = {}

    # Parse through ability table and extract the ability name and text.
    for row in ability_table.find_all('tr'):
        columns = row.find_all('td')

        if len(columns) >= 2:
            ability_name = columns[1].text.strip()

        file_object = open("text_files/abilities.txt", "w+")
        file_object.write(ability_name + "\n")
        file_object.close()


