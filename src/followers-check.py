import json
import bs4
from bs4 import BeautifulSoup

class InstaDataParser:
    """ class to parse instagram followers + following information from JSON or HTML export files. """

    def __init__(self):
        self.followers = []
        self.following = []

    def load_from_json(self, followers_path, following_path):
        """ loads followers and following lists from JSON file export. """
        with open(followers_path, 'r', encoding='utf-8') as followers_json:
            followers_data = json.load(followers_json)
        self.followers = [follower['string_list_data'][0]['value'] for follower in followers_data]

        with open(following_path, 'r', encoding='utf-8') as following_json:
            following_data = json.load(following_json)
        self.following = [following['string_list_data'][0]['value'] for following in following_data]

    def load_from_html(self, followers_html_path, following_html_path):
        """ loads followers list from an Instagram HTML file export. """
        with open(followers_html_path, 'r', encoding='utf-8') as followers_html:
            soup_followers = BeautifulSoup(followers_html, 'html.parser')
        self.followers = [a.text.strip() for a in soup_followers.find_all('a') if a.text.strip()]

        with open(following_html_path, 'r', encoding='utf-8') as following_html:
            soup_following = BeautifulSoup(following_html, 'html.parser')
        self.following = [a.text.strip() for a in soup_following.find_all('a') if a.text.strip()]

    def analyze(self):
        """ returns mutuals, people who don't follow you, and people you don't follow."""
        followers_set = set(self.followers)
        following_set = set(self.following)

        mutual = list(followers_set & following_set)
        not_following_you_back = list(following_set - followers_set)
        you_dont_follow_back = list(followers_set - following_set)

        return mutual, not_following_you_back, you_dont_follow_back
    
    def print_full_list(self, mutual, not_following_you_back, you_dont_follow_back):
        print("mutuals:", mutual)
        print("people who don't follow you back:", not_following_you_back)
        print("people who you don't follow back:", you_dont_follow_back)
    
    def export_txt(self, mutual, not_following_you_back, you_dont_follow_back):
        with open('./out/mutuals.txt', 'w', encoding='utf-8') as mutuals_file:
            for m in mutual:
                mutuals_file.write(m + '\n')
        print("saved your mutuals to out/mutuals.txt")

        with open('./out/not_following_you_back.txt', 'w', encoding='utf-8') as not_following_you_back_file:
            for t in not_following_you_back:
                not_following_you_back_file.write(t + '\n')
        print("saved the people who don't follow you back to out/dont_follow_you_back.txt")

        with open('./out/you_dont_follow_back.txt', 'w', encoding='utf-8') as you_dont_follow_back_file:
            for y in you_dont_follow_back:
                you_dont_follow_back_file.write(y + '\n')
        print("saved the people you don't follow back to out/you_dont_follow_back.txt")


def main():
    parser = InstaDataParser()

    file_format = input("are your instagram files in 'json' or 'html' format?\n").strip().lower()

    if file_format == 'html':
        parser.load_from_html('./followers_and_following/followers_1.html', './followers_and_following/following.html')
    elif file_format == 'json':
        parser.load_from_json('./followers_and_following/followers.json', './followers_and_following/followings.json')
    else:
        print("invalid choice. please enter 'json' or 'html'.")
        return
    
    mutual, not_following_you_back, you_dont_follow_back = parser.analyze()

    print("\n")
    print("STATISTICS")
    print("amount of mutuals: ", len(mutual))
    print("amount of people who don't follow you back: ", len(not_following_you_back))
    print("amount of people who you don't follow back: ", len(you_dont_follow_back))
    print("\n")

    # TO DIRECTLY PRINT THE FULL LISTS, UNCOMMENT THE LINE BELOW
    # parser.print_full_list(mutual, not_following_you_back, you_dont_follow_back)

    parser.export_txt(mutual, not_following_you_back, you_dont_follow_back)


if __name__ == "__main__":
    main()