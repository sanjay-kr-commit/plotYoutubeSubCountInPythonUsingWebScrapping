import requests
import re

def sub_count( page_url ) -> int :
    page = requests.get(page_url)

    if page.status_code != 200:
        print("Error : Page Response is not 200 ", page.status_code)
        exit(-1)

    strPage = str(page.content)

    result = re.findall("\"content\":\"[0-9]+.?[0-9]*[mMkK]? ?subscribers?\"", strPage)

    if not result:
        return 0

    subscribers = str(result[0])

    result = re.findall("[0-9]+.?[0-9]*[mMkK]?", subscribers)

    if not result:
        return 0

    count = str(result[0])

    length = len(count)

    num = float(str(re.findall("[0-9]+.?[0-9]*", count)[0]))

    if count[length - 1] == 'k' or count[length - 1] == 'K':
        num *= 1000
    elif count[length - 1] == 'm' or count[length - 1] == 'M':
        num *= 1000000
    elif count[length - 1] == 'b' or count[length - 1] == 'B':
        num *= 1000000000

    return int(num)

if __name__ == "__main__":
    page_url = "https://www.youtube.com/@Fireship"
    print( sub_count(page_url) )