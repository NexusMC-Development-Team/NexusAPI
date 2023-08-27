import requests

class NexusMCDefault:
    def __init__(self, api_base_url="https://api.nexusmc.world"):
        self.api_base_url = api_base_url

    def get_user_by_uuid(self, uuid):
        url = f"{self.api_base_url}/user/uuid/{uuid}"
        response = requests.get(url)
        return response.json()

    def get_user_by_username(self, username):
        url = f"{self.api_base_url}/user/username/{username}"
        response = requests.get(url)
        return response.json()

class NexusMCRanks:
    def __init__(self, api_base_url="https://api.nexusmc.world"):
        self.api_base_url = api_base_url
        
    def get_player_rank_by_username(self, username):
        url = f"{self.api_base_url}/rank/username/{username}"
        response = requests.get(url)
        return response.json()

    def get_player_rank_by_uuid(self, uuid):
        url = f"{self.api_base_url}/rank/uuid/{uuid}"
        response = requests.get(url)
        return response.json()

class NexusMCFriends:
    def __init__(self, api_base_url="https://api.nexusmc.world"):
        self.api_base_url = api_base_url
    
    def get_user_friends_by_uuid(self, uuid):
        url = f"{self.api_base_url}/user/friends/uuid/{uuid}"
        response = requests.get(url)
        return response.json()

    def get_user_friends_by_username(self, username):
        url = f"{self.api_base_url}/user/friends/username/{username}"
        response = requests.get(url)
        return response.json()
