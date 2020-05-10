import requests


SPOTIFY_ENDPOINT  = 'https://api.spotify.com'
SEARCH_ENDPOINT = '/v1/search'

SPOTIFY_TOKEN = "BQDp4Xv8SFM6r0h4ceOBTy5n5msqRcm3CMfb1RZPlmqkHBdw6CrwIf-P8umvbcXOO_8isZhIEwQt12DCDmw"

request_headers = {
                'content-type': "application/json"
                }


def parse_track(item):
    name = item['name']
    thumbnail_links = item.get('album', {}).get('images')
    smallest_image_width = 640
    image = None
    for thumb in thumbnail_links:
        if not thumb['width'] or not thumb['height']:
            continue
        if thumb['width'] < smallest_image_width and thumb['width'] >= 64 and thumb['height'] >= 64:
            image = thumb['url']
            smallest_image_width = thumb['width']
    return {
        'name': name,
        'image': image,
    }

def parse_other_items(item):
    name = item['name']
    image = None
    smallest_image_width = 640
    thumbnail_links = item.get('images', [])
    for thumb in thumbnail_links:
        if not thumb['width'] or not thumb['height']:
            continue
        if thumb['width'] < smallest_image_width and thumb['width'] >= 64 and thumb['height'] >= 64:
            image = thumb['url']
            smallest_image_width = thumb['width']

    return {
        'name': name,
        'image': image
    }


def parse_item(item, item_type):
    if item_type == 'track':
        return parse_track(item)
    else:
        return parse_other_items(item)



def get_track_list(search_query, query_filter='track', limit=20, offset=0):
    if search_query is None or '':
        return 0, []
    
    if limit < offset:
        return 0, []

    if limit > 100000:
        return 0, []

    valid_query_filters = ['track', 'album', 'playlist', 'artist']
    if query_filter not in valid_query_filters:
        return 0, []
    
    if not search_query:
        search_query = "crash"

    request_params = {
        'q' : search_query,
        'type' : query_filter,
        'limit': limit,
        'offset': offset,
        'access_token': SPOTIFY_TOKEN
    }

    api_endpoint = SPOTIFY_ENDPOINT + SEARCH_ENDPOINT
    response = requests.get(api_endpoint, headers=request_headers, params=request_params )

    if response.status_code == requests.codes.ok:
        response_object = response.json()
        key = query_filter + 's'
        count = response_object[key].get('total', 0)
        response_items = response_object[key].get('items')

        items = [parse_item(item, item_type=query_filter) for item in response_items]
        return count, items

    else:
        return 0, []