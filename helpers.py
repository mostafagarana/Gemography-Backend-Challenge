import requests
from datetime import datetime, timedelta


def get_langs(url):
    """Returns languages' name."""

    try:
        json_langs = requests.get(url).json()
    except Exception as e:
        print("Something went wrong...\n", e)
    else:
        langs = [lang for lang in json_langs.keys()]
        return langs


def github_trending_api(page):
    """Returns json object of most starred repos created in the last 30 days."""

    url = 'https://api.github.com/search/repositories?q=created:>%s&sort=stars&order=desc&page=%d'
    date = (datetime.today() - timedelta(days=30)).strftime('%Y-%m-%d')
    try:
        response = requests.get(url % (date, page))
    except Exception as e:
        print("Something went wrong...\n", e)
    else:
        json_response = response.json()

        return json_response


def languages_dictionary():
    """Returns a dict of each language and repos using it."""

    langs_dict = {}
    page, repos = 1, 0
    while True:
        json_response = github_trending_api(page)
        page += 1
        if json_response:
            for item in json_response['items']:
                repos += 1
                for lang in get_langs(item['languages_url']):
                    if lang not in langs_dict.keys():
                        langs_dict[lang] = [item['url']]
                    else:
                        langs_dict[lang].append(item['url'])
                if repos == 100:
                    return [
                            {'language': key, 'number_of_repos': len(langs_dict[key]), 'repos': langs_dict[key]}
                            for key in langs_dict.keys()
                           ]
