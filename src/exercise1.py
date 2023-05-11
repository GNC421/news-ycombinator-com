############################################################################################################
#Filter all previous entries with more than five words in the title ordered by the number of comments first#

import requests

def get30Entries():
    #I use this API to get the top news in https://news.ycombinator.com/
    resp = requests.get('https://hacker-news.firebaseio.com/v0/topstories.json')

    #I get only the first 30 entries of the list
    list = resp.json()[:30]
    array = []
    for index in list:
        array.append(requests.get('https://hacker-news.firebaseio.com/v0/item/'+str(index)+'.json').json())

    return array


def main():
    array = get30Entries()


if __name__ == '__main__':
    main()