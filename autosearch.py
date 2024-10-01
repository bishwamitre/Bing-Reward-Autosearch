import wikipedia
import random
import webbrowser
import time
import num2words

class RewardSearch:
    def __init__(self):
        self.page = wikipedia.random(pages=1)
        self.url = f"https://www.bing.com/search?q={self.page}&FORM=AWRE"

    def open_web_page(self):
        webbrowser.open_new_tab(self.url)

    def get_integer(self):
        while True:
            try:
                num = int(input("Enter a positive integer: "))
                if num <= 0:
                    print("Please enter a positive integer.")
                else:
                    return num
            except ValueError:
                print("Please enter a valid number. Try again!")

    def engine(self, n):
        for count in range(1, n+1):
            word = num2words.num2words(count)
            word = str(word).capitalize()
            U = (f"{word} searches has performed.")
            print("{:^40}".format(U))
            self.open_web_page()
            sleep_time_range = (25, 40)  # Configurable sleep time range
            if count != n:
                sleep_time = random.randint(*sleep_time_range)
                time.sleep(sleep_time)
            else:
                break

    def main(self):
        try:
            number = self.get_integer()
            print("{:-^40}".format("STARTED"))
            self.engine(number)
            print("{:-^40}".format("FINISHED"))
        except KeyboardInterrupt or EOFError:
            print("\nInterrupted by user!")


if __name__ == "__main__":
    search = RewardSearch()
    search.main()
