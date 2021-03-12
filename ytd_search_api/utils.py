from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

DEVELOPER_KEY = "AIzaSyCRl-64fxsgM8YjORV3-eprM71S-wnPJJE"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"




def youtube_search(q, max_results=10,order="relevance", token=None, location=None, location_radius=None):
    """
    youtube api query by default it limited to 10 results
    """
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=DEVELOPER_KEY)

    search_response = youtube.search().list(
    q=q,
    type="video",
    pageToken=token,
    order = order,
    part="id,snippet",
    maxResults=max_results,
    location=location,
    locationRadius=location_radius

    ).execute()
    videos = []
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append(search_result)
    try:
        nexttok = search_response["nextPageToken"]
        return(nexttok, videos)
    except Exception as e:
        nexttok = "last_page"
        return(nexttok, videos)


def json_serialization(ytd_json_op):
    """
    helping func for json serialize (filtering only required data)
    """
    ytd_data_array = []
    for r_obj in ytd_json_op:
        ytd_data_array.append(
        {
            'link': 'https://www.youtube.com/watch?v='+ r_obj['id']['videoId'],
            'title': r_obj['snippet']['title'],
            'image': r_obj['snippet']['thumbnails']['medium']['url'],
            'description': r_obj['snippet']['description'],
            'channel_link': 'https://www.youtube.com/channel/'+r_obj['snippet']['channelId'],
            'published_at': r_obj['snippet']['publishedAt']
        })
    return ytd_data_array
