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
