"""
Wikipedia Module
================

This module provides functionality to fetch and clean cocktail ingredients from Wikipedia.

Functions:
----------
- get_cocktail_ingredients(cocktail_wikipedia: str) -> list[str] | None:
    Fetches and cleans cocktail ingredients from the specified Wikipedia page.

Dependencies:
-------------
- wptools: Used to fetch and parse Wikipedia pages.

Usage:
------
To fetch and clean cocktail ingredients, call the `get_cocktail_ingredients` function with the Wikipedia page title of the cocktail. The function returns a list of cleaned ingredients if found, otherwise None.

Example:
--------
>>> from wikipedia import get_cocktail_ingredients
>>> ingredients = get_cocktail_ingredients("Margarita")
>>> if ingredients:
>>>     for ingredient in ingredients:
>>>         print(ingredient)
Tequila
Triple sec
Lime juice
Salt
"""

import wptools


def get_cocktail_ingredients(cocktail_wikipedia: str) -> list[str] | None:
    """
    Fetches and cleans cocktail ingredients from Wikipedia.

    :param cocktail_wikipedia: The Wikipedia page title for the cocktail.

    :return: A list of cleaned ingredients if found, otherwise None.
    """
    try:
        # Fetch the Wikipedia page
        page = wptools.page(cocktail_wikipedia).get_parse()
        ingredients = page.data['infobox']["ingredients"]

        # Clean the ingredients by removing unwanted characters
        cleaned_ingredients = [
            ingredient.replace("&nbsp;", " ").replace("[[", "").replace("]]", "").strip()
            for ingredient in ingredients.split("\n")
        ]

        return cleaned_ingredients if cleaned_ingredients else None

    except KeyError:
        print(f"No ingredients found in the infobox for {cocktail_wikipedia}.")

    except Exception as e:
        print(f"Error fetching cocktail ingredients: {e}")

    return None
