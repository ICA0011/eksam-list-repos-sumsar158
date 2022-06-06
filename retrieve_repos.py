import json
import requests

username = "talisainen"


def retrieve_repos(username):

    url = "https://api.github.com/users/" + username + "/repos"

    result = json.loads(requests.get(url).text)

    print(result)
    return len(result)
