import requests

from menu import Menus
from pages.english_page import EnglishPage

LEVEL_URLS = {
    'b': 'nivel-basico',
    'i': 'nivel-intermedio',
    'a': 'nivel-avanzado',
    'biz': 'ingles-negocios',
    't': 'vocabulario-viajar'
}

print(Menus.LEVEL_OPTIONS)
user_choice = input("What level of English would you like? ")
while user_choice != 'q':
    try:
        page_content = requests.get(f'http://curso-ingles.com/aprender/cursos/{LEVEL_URLS[user_choice]}').content
    except KeyError:
        print(f'<{user_choice}> is not a valid input, please try again.')
    else:
        page = EnglishPage(page_content)
        page.print_random_topic()
        page.print_continue_menu()
    finally:
        print(Menus.LEVEL_OPTIONS)
        user_choice = input("What level of English would you like? ")
