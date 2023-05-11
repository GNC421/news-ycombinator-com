###################################################################################################
#Filter all previous entries with less than or equal to five words in the title ordered by points.#

import requests
from exercise1 import get30Entries

#filter by title
def filterByTitle(array):
    result = []
    for index in array:
        if len(index['title'].split())<=5:
            result.append(index)
    return result

def main():
    array = get30Entries()
    filtered = filterByTitle(array)

if __name__ == '__main__':
    main()