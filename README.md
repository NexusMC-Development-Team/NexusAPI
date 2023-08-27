# NexusMC API Client Documentation

This is outdated, I would check the Wiki.

The NexusAPI will allow you to lookup open player data that is not sensitive info. This includes colectables, ext. Please do not find a way to abuse this. This is for testing purpuses only. We will block spam from IP's, this will count as being blocked on the network as well.

First, to use the API you will need to install our client. To do this do `git clone https://github.com/NexusMC-Development-Team/NexusAPI/` and then `cd NexusAPI`. Then you can make a simple python script like below.

Example Script:
```python
from package import NexusMCDefault, NexusMCRanks

api_client = NexusMCDefault()
ranks = NexusMCRanks()

# Example usage
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
{'UUID': 'a049df05-4833-4eb9-ba71-ba59d3645cf8', 'Name': 'RailenBailen', 'Mystery_Dust': 0, 'Mystery_Gift_Packs': 0, 'Mystery_Gift_Sent': 0, 'Mystery_Gift_Received': 0, 'Pet_Name': "§bRailenBailen's pet", 'Self_Morph_View': 'true', 'Bypass_Cooldown': 'false', 'Mystery_Vault_Animation': 'Normal', 'Recent_Loots_Found': '', 'Selected_Hat': 'none', 'Selected_Animated_Hat': 'none', 'Selected_Particle': 'none', 'Selected_Suit_Helmet': 'Spooderman Helmet', 'Selected_Suit_Chestplate': 'Spooderman Chestplate', 'Selected_Suit_Leggings': 'Spooderman Leggings', 'Selected_Suit_Boots': 'Spooderman Boots', 'Selected_Gadget': 'Trampoline', 'Selected_Pet': 'none', 'Selected_Morph': 'none', 'Selected_Banner': 'none', 'Selected_Emote': 'none', 'Selected_Cloak': 'none'}
---------------------------------
{'UUID': 'a049df05-4833-4eb9-ba71-ba59d3645cf8', 'Name': 'RailenBailen', 'Mystery_Dust': 0, 'Mystery_Gift_Packs': 0, 'Mystery_Gift_Sent': 0, 'Mystery_Gift_Received': 0, 'Pet_Name': "§bRailenBailen's pet", 'Self_Morph_View': 'true', 'Bypass_Cooldown': 'false', 'Mystery_Vault_Animation': 'Normal', 'Recent_Loots_Found': '', 'Selected_Hat': 'none', 'Selected_Animated_Hat': 'none', 'Selected_Particle': 'none', 'Selected_Suit_Helmet': 'Spooderman Helmet', 'Selected_Suit_Chestplate': 'Spooderman Chestplate', 'Selected_Suit_Leggings': 'Spooderman Leggings', 'Selected_Suit_Boots': 'Spooderman Boots', 'Selected_Gadget': 'Trampoline', 'Selected_Pet': 'none', 'Selected_Morph': 'none', 'Selected_Banner': 'none', 'Selected_Emote': 'none', 'Selected_Cloak': 'none'}
---------------------------------
{'uuid': 'a049df05-4833-4eb9-ba71-ba59d3645cf8', 'username': 'railenbailen', 'rank': 'owner'}
---------------------------------
{'uuid': 'a049df05-4833-4eb9-ba71-ba59d3645cf8', 'username': 'railenbailen', 'rank': 'owner'}
---------------------------------
```

