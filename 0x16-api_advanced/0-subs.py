#!/usr/bin/python3
"""Function to query subscribers on a given Reddit subreddit."""
import requests

def number_of_subscribers(subreddit):
    
    # Define the URL for the subreddit's about.json page
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Set custom User-Agent to avoid being blocked by Reddit's servers
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    # headers = {'User-Agent': 'Mozilla/5.0 (compatible; RedditAPI/0.1;
    # +http://www.example.com/bot)'}
    
    # Send a GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the status code indicates success
    if response.status_code == 200:
        # Parse the response as JSON and extract the subscriber count
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        # If the subreddit is invalid or the request failed, return 0
        return 0
