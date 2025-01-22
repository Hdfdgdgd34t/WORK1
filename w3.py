from telethon import TelegramClient
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
API_ID = 123
API_HASH = ''
PHONE_NUMBER = ''
SESSION_NAME = 'my_session'
def initialize_client():
    return TelegramClient(SESSION_NAME, API_ID, API_HASH)
async def fetch_channel_participants(client, channel_username, limit=2):
    try:
        channel = await client.get_entity(channel_username)
        participants = await client(GetParticipantsRequest(
            channel=channel,
            filter=ChannelParticipantsSearch(''),
            offset=0,
            limit=limit,
            hash=0
        ))
        return participants.users
    except Exception as e:
        print(f"Error fetching participants: {e}")
        return []
async def send_test_message(client, message):
    try:
        await client.send_message('123', message)
        print("Message sent successfully.")
    except Exception as e:
        print(f"Error sending message: {e}")
async def main():
    async with initialize_client() as client:
        channel_username = '1234'
        participants = await fetch_channel_participants(client, channel_username)
        for user in participants:
            print(user.id, user.first_name, user.last_name)
        await send_test_message(client, "TEST")
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())