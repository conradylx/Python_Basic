import re
import webbrowser
from urllib.error import URLError


def check_correctness_of_url(user_url):
    regex = re.compile(
        r'^((http|ftp|https)://)?([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?', re.IGNORECASE)

    try:
        if re.search(regex, user_url):
            webbrowser.open(user_url)
        else:
            raise URLError
    except (TypeError, URLError):
        print("Given url is invalid.")


if __name__ == '__main__':
    user_url = input("Enter url: ")
    check_correctness_of_url(user_url)
