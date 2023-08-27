import requests
import time

class NexusMCDefault:
    def __init__(self, api_base_url="https://api.nexusmc.world"):
        self.api_base_url = api_base_url

    def get_user_by_uuid(self, uuid):
        url = f"{self.api_base_url}/user/uuid/{uuid}"
        response = self._get_with_ratelimit_notification(url)
        return response.json()

    def get_user_by_username(self, username):
        url = f"{self.api_base_url}/user/username/{username}"
        response = self._get_with_ratelimit_notification(url)
        return response.json()

    def _get_with_ratelimit_notification(self, url):
        response = requests.get(url)
        if response.status_code == 429:
            print("You are being rate-limited. Please try again later.")
            retry_after = int(response.headers.get("Retry-After", 3))
            time.sleep(retry_after)
            response = self._get_with_ratelimit_notification(url)
        return response

class NexusMCRanks:
    def __init__(self, api_base_url="https://api.nexusmc.world"):
        self.api_base_url = api_base_url

    def get_player_rank_by_username(self, username):
        url = f"{self.api_base_url}/rank/username/{username}"
        response = self._get_with_ratelimit_notification(url)
        return response.json()

    def get_player_rank_by_uuid(self, uuid):
        url = f"{self.api_base_url}/rank/uuid/{uuid}"
        response = self._get_with_ratelimit_notification(url)
        return response.json()

    def _get_with_ratelimit_notification(self, url):
        response = requests.get(url)
        if response.status_code == 429:
            print("You are being rate-limited. Please try again later.")
            retry_after = int(response.headers.get("Retry-After", 3))
            time.sleep(retry_after)
            response = self._get_with_ratelimit_notification(url)
        return response

class NexusMCFriends:
    def __init__(self, api_base_url="https://api.nexusmc.world"):
        self.api_base_url = api_base_url

    def get_user_friends_by_uuid(self, uuid):
        url = f"{self.api_base_url}/user/friends/uuid/{uuid}"
        response = self._get_with_ratelimit_notification(url)
        return response.json()

    def get_user_friends_by_username(self, username):
        url = f"{self.api_base_url}/user/friends/username/{username}"
        response = self._get_with_ratelimit_notification(url)
        return response.json()

    def _get_with_ratelimit_notification(self, url):
        response = requests.get(url)
        if response.status_code == 429:
            print("You are being rate-limited. Please try again later.")
            retry_after = int(response.headers.get("Retry-After", 3))
            time.sleep(retry_after)
            response = self._get_with_ratelimit_notification(url)
        return response
