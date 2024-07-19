# Bing-Reward-auto-search
###### Random Wikipedia Page Searcher with Bing Rewards
This Python script automates the process of generating random Wikipedia pages and searching for them on Bing. It uses the wikipedia library to fetch random Wikipedia pages, constructs a special search URL for Bing Rewards, and opens the search results in a new browser tab.

### Features:
- Generates random Wikipedia pages.
- Constructs Bing search URLs for the generated pages.
- Opens search results in a new browser tab.
- Configurable number of searches and sleep time range between searches.
- Handles exceptions and provides user-friendly error messages.

### Usage:
- 1.Run the script.
- 2.Enter the number of searches you want to perform.
- 3.The script will automatically generate random Wikipedia pages, search for them on Bing, and open the results in your `default web browser`.

### Requirements:
- `wikipedia` library
- `webbrowser` module (standard library)
- `random` module (standard library)
- `time` module (standard library)