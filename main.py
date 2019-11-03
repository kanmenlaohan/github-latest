import sys
import json

import requests

# Use Like python githubber.py JASchilz
# (or another user name)

if __name__ == "__main__":
    username = sys.argv[1]
    # print(username)
    response = requests.get("https://api.github.com/users/{}/events".format(username))
    creation_date = response.json()[0]["payload"]["forkee"]["created_at"]
    # TODO:
    #
    # 1. Retrieve a list of "events" associated with the given user name
    # 2. Print out the time stamp associated with the first event in that list.

    print("{} lastes event is at {}".format(username, creation_date))
