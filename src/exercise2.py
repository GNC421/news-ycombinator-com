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

#definition of sort's criteria
def MyCriteria(e):
    return e['score']

def main():
    array = get30Entries()
    filtered = filterByTitle(array)
    #order by number of comments
    filtered.sort(key=MyCriteria)
    #Here we have the first exercise's result
    print(filtered)

if __name__ == '__main__':
    main()