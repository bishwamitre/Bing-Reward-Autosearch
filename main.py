import wikipedia
import random
import webbrowser
import time

def generate_random_page():
    return wikipedia.random(pages=1)

def create_url(page):
    return f"https://www.bing.com/search?q={page.replace(' ', '+')}&FORM=AWRE"

def open_web_page(url):
    webbrowser.open_new_tab(url)

def main(n, sleep_time_range):
    print('-' * 40)
    try:
        for count, _ in enumerate(range(n), start=1):
            print(f"...searches performed: {count}")
            page = generate_random_page()
            url = create_url(page)
            open_web_page(url)
            sleep_time = random.randint(*sleep_time_range)
            time.sleep(sleep_time)
    except Exception as e:
        print(f"An error occurred: {e}")
    print('-' * 40)
    print("Finished!")

def search():
    try:
        search = int(input("Number of Search: "))
        sleep_time_range = (10, 20)  # Configurable sleep time range
        main(search, sleep_time_range)
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    search()