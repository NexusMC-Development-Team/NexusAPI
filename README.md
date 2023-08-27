# NexusMC API Client Documentation

This is outdated, I would check the Wiki.

The NexusAPI will allow you to lookup open player data that is not sensitive info. This includes colectables, ext. Please do not find a way to abuse this. This is for testing purpuses only. We will block spam from IP's, this will count as being blocked on the network as well.

First, to use the API you will need to install our client. To do this do `git clone https://github.com/NexusMC-Development-Team/NexusAPI/` and then `cd NexusAPI`. Then you can make a simple python script like below.

Example Script:
```python
from NexusMC import nexusmc_api

# Initialize API clients
default_api = nexusmc_api.NexusMCDefault()
ranks_api = nexusmc_api.NexusMCRanks()
friends_api = nexusmc_api.NexusMCFriends()

# Example usage
uuid = "a049df05-4833-4eb9-ba71-ba59d3645cf8"
username = "railenbailen"

user_data_by_uuid = default_api.get_user_by_uuid(uuid)
user_data_by_username = default_api.get_user_by_username(username)

rank_data_by_username = ranks_api.get_player_rank_by_username(username)
rank_data_by_uuid = ranks_api.get_player_rank_by_uuid(uuid)

user_friends_by_uuid = friends_api.get_user_friends_by_uuid(uuid)
user_friends_by_username = friends_api.get_user_friends_by_username(username)

print("User Data by UUID:", user_data_by_uuid)
print("User Data by Username:", user_data_by_username)
print("Rank Data by Username:", rank_data_by_username)
print("Rank Data by UUID:", rank_data_by_uuid)
print("User Friends by UUID:", user_friends_by_uuid)
print("User Friends by Username:", user_friends_by_username)
print("")

# Example usage with api_client and ranks
api_client = nexusmc_api.NexusMCDefault()
ranks = nexusmc_api.NexusMCRanks()

uuid_data = api_client.get_user_by_uuid("a049df05-4833-4eb9-ba71-ba59d3645cf8")
print(uuid_data)
print("---------------------------------")

username_data = api_client.get_user_by_username("RailenBailen")
print(username_data)
print("---------------------------------")

rank_by_username = ranks.get_player_rank_by_username("RailenBailen")
print(rank_by_username)
print("---------------------------------")

rank_by_uuid = ranks.get_player_rank_by_uuid("a049df05-4833-4eb9-ba71-ba59d3645cf8")
print(rank_by_uuid)
print("---------------------------------")
```

Example Output:

```output
User Data by UUID: {'UUID': 'a049df05-4833-4eb9-ba71-ba59d3645cf8', 'Name': 'RailenBailen', 'Mystery_Dust': 0, 'Mystery_Gift_Packs': 0, 'Mystery_Gift_Sent': 0, 'Mystery_Gift_Received': 0, 'Pet_Name': "§bRailenBailen's pet", 'Self_Morph_View': 'true', 'Bypass_Cooldown': 'false', 'Mystery_Vault_Animation': 'Normal', 'Recent_Loots_Found': '', 'Selected_Hat': 'none', 'Selected_Animated_Hat': 'none', 'Selected_Particle': 'none', 'Selected_Suit_Helmet': 'none', 'Selected_Suit_Chestplate': 'none', 'Selected_Suit_Leggings': 'none', 'Selected_Suit_Boots': 'none', 'Selected_Gadget': 'none', 'Selected_Pet': 'none', 'Selected_Morph': 'none', 'Selected_Banner': 'none', 'Selected_Emote': 'none', 'Selected_Cloak': 'none'}
User Data by Username: {'UUID': 'a049df05-4833-4eb9-ba71-ba59d3645cf8', 'Name': 'RailenBailen', 'Mystery_Dust': 0, 'Mystery_Gift_Packs': 0, 'Mystery_Gift_Sent': 0, 'Mystery_Gift_Received': 0, 'Pet_Name': "§bRailenBailen's pet", 'Self_Morph_View': 'true', 'Bypass_Cooldown': 'false', 'Mystery_Vault_Animation': 'Normal', 'Recent_Loots_Found': '', 'Selected_Hat': 'none', 'Selected_Animated_Hat': 'none', 'Selected_Particle': 'none', 'Selected_Suit_Helmet': 'none', 'Selected_Suit_Chestplate': 'none', 'Selected_Suit_Leggings': 'none', 'Selected_Suit_Boots': 'none', 'Selected_Gadget': 'none', 'Selected_Pet': 'none', 'Selected_Morph': 'none', 'Selected_Banner': 'none', 'Selected_Emote': 'none', 'Selected_Cloak': 'none'}
Rank Data by Username: {'uuid': 'a049df05-4833-4eb9-ba71-ba59d3645cf8', 'username': 'railenbailen', 'rank': 'penguin'}
Rank Data by UUID: {'uuid': 'a049df05-4833-4eb9-ba71-ba59d3645cf8', 'username': 'railenbailen', 'rank': 'penguin'}
User Friends by UUID: []
User Friends by Username: [{'player_name': 'RailenBailen', 'player_uuid': 'a049df05-4833-4eb9-ba71-ba59d3645cf8'}, {'player_name': 'StalkingWoolf', 'player_uuid': 'e9eb40c3-0cf2-492f-bffc-23f1b7fa2119'}, {'player_name': 'Goofyorangee', 'player_uuid': '34af9345-7272-42a4-83e5-3cdce5182bd6'}]

{'UUID': 'a049df05-4833-4eb9-ba71-ba59d3645cf8', 'Name': 'RailenBailen', 'Mystery_Dust': 0, 'Mystery_Gift_Packs': 0, 'Mystery_Gift_Sent': 0, 'Mystery_Gift_Received': 0, 'Pet_Name': "§bRailenBailen's pet", 'Self_Morph_View': 'true', 'Bypass_Cooldown': 'false', 'Mystery_Vault_Animation': 'Normal', 'Recent_Loots_Found': '', 'Selected_Hat': 'none', 'Selected_Animated_Hat': 'none', 'Selected_Particle': 'none', 'Selected_Suit_Helmet': 'none', 'Selected_Suit_Chestplate': 'none', 'Selected_Suit_Leggings': 'none', 'Selected_Suit_Boots': 'none', 'Selected_Gadget': 'none', 'Selected_Pet': 'none', 'Selected_Morph': 'none', 'Selected_Banner': 'none', 'Selected_Emote': 'none', 'Selected_Cloak': 'none'}
---------------------------------
{'UUID': 'a049df05-4833-4eb9-ba71-ba59d3645cf8', 'Name': 'RailenBailen', 'Mystery_Dust': 0, 'Mystery_Gift_Packs': 0, 'Mystery_Gift_Sent': 0, 'Mystery_Gift_Received': 0, 'Pet_Name': "§bRailenBailen's pet", 'Self_Morph_View': 'true', 'Bypass_Cooldown': 'false', 'Mystery_Vault_Animation': 'Normal', 'Recent_Loots_Found': '', 'Selected_Hat': 'none', 'Selected_Animated_Hat': 'none', 'Selected_Particle': 'none', 'Selected_Suit_Helmet': 'none', 'Selected_Suit_Chestplate': 'none', 'Selected_Suit_Leggings': 'none', 'Selected_Suit_Boots': 'none', 'Selected_Gadget': 'none', 'Selected_Pet': 'none', 'Selected_Morph': 'none', 'Selected_Banner': 'none', 'Selected_Emote': 'none', 'Selected_Cloak': 'none'}
---------------------------------
{'uuid': 'a049df05-4833-4eb9-ba71-ba59d3645cf8', 'username': 'railenbailen', 'rank': 'penguin'}
---------------------------------
{'uuid': 'a049df05-4833-4eb9-ba71-ba59d3645cf8', 'username': 'railenbailen', 'rank': 'penguin'}
---------------------------------
```

