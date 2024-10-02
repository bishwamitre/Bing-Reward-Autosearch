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

def get_integer():
    while True:
        try:
            num = int(input("Enter a positive integer: "))
            if num <= 0:
                print("Please enter a positive integer.")
            else:
                return num
        except ValueError:
            print("Please enter a valid number. Try again!")

def engine(n):
    for count in range(1, n+1):
        prompt = (f"{count} searches has performed.")
        print("{:^40}".format(prompt))
        page = generate_random_page()
        url = create_url(page)
        open_web_page(url)
        sleep_time_range = (25, 40)  # Configurable sleep time range
        if count != n:
            sleep_time = random.randint(*sleep_time_range)
            time.sleep(sleep_time)
        else:
            break

def main():
    try:
        number = get_integer()
        print("{:-^40}".format("STARTED"))
        engine(number)
        print("{:-^40}".format("FINISHED"))
    except KeyboardInterrupt or EOFError:
        print("\nInterrupted by user!")


if __name__ == "__main__":
    main()
