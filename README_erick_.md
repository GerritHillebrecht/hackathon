""" click edit to access the code """ 


import requests
from bs4 import BeautifulSoup
from cocktails import cocktails

def get_cocktail_ingredients(cocktail_wikipedia):
    """
    Fetches and cleans cocktail ingredients from Wikipedia using BeautifulSoup.

    Args:
        cocktail_wikipedia (str): The Wikipedia page title for the cocktail.

    Returns:
        list: A list of cleaned ingredients if found, otherwise None.
    """
    """ """
    try:
        url = f"https://en.wikipedia.org/wiki/{cocktail_wikipedia}"
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors

        soup = BeautifulSoup(response.text, 'html.parser')
        infobox = soup.find('table', {'class': 'infobox'})

        if not infobox:
            return None

        ingredients = []
        for row in infobox.find_all('tr'):
            header = row.find('th')
            if header and 'ingredients' in header.get_text().lower():
                content = row.find('td')
                if content:
                    for item in content.find_all(['li', 'p']):
                        text = item.get_text(strip=True)
                        if text:
                            ingredients.append(text)

        return ingredients if ingredients else None
    except Exception as e:
        print(f"Error fetching ingredients: {e}")
        return None
