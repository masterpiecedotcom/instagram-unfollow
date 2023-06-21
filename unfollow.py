import requests

def check_who_doesnt_follow_me_back():
  """Returns a list of users who don't follow you back on Instagram."""
  url = "https://www.instagram.com/me/following"
  response = requests.get(url)
  if response.status_code == 200:
    following_data = response.json()
    followers_data = requests.get(
        "https://www.instagram.com/me/followers").json()
    following_ids = [user["id"] for user in following_data]
    followers_ids = [user["id"] for user in followers_data]
    unfollowed_ids = [id for id in following_ids if id not in followers_ids]
    return unfollowed_ids
  else:
    return []

def delete_users(unfollowed_ids):
  """Deletes the users in the given list from your Instagram following list."""
  for id in unfollowed_ids:
    url = f"https://www.instagram.com/web/friendships/{id}/unfollow/"
    requests.post(url)

unfollowed_ids = check_who_doesnt_follow_me_back()
delete_users(unfollowed_ids)
