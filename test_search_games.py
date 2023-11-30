from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import requests
from bs4 import BeautifulSoup
from database.database import Product


engine = create_engine('sqlite:///instance/products.db')
Session = sessionmaker(bind=engine)
session = Session()


def scrape_steam_games(base_url, pages=5):
    for page in range(1, pages + 1):
        url = f"{base_url}&page={page}"

        response = requests.get(url)
        if response.status_code != 200:
            print('Nie udało się pobrać strony:', url)
            continue

        soup = BeautifulSoup(response.text, 'html.parser')
        game_entries = soup.find_all('a', {'class': 'search_result_row'})

        for game in game_entries:
            try:
                title_element = game.find('span', {'class': 'title'})
                image_element = game.find('div', {'class': 'col search_capsule'}).find('img')
                price_element = game.find('div', {'class': 'discount_final_price'})

                title = title_element.text if title_element else "Brak tytułu"
                image_url = image_element['src'] if image_element else "Brak obrazka"
                price_text = price_element.text if price_element else "Free"

                if price_text != "Free":
                    price_text = price_text.replace(' zł', '').replace(',', '.')
                    price = float(price_text)
                else:
                    price = 0.0

                existing_product = session.query(Product).filter_by(name=title).first()
                if existing_product is None:
                    product = Product(name=title, description="", price=price, available=True, image=image_url)
                    session.add(product)
                else:
                    print(f"Gra '{title}' już istnieje w bazie danych.")
            except Exception as e:
                print(f'Błąd przy przetwarzaniu gry: {e}')

        session.commit()



session.close()

steam_url = 'https://store.steampowered.com/search/?filter=topsellers'
scrape_steam_games(steam_url, pages=50)
