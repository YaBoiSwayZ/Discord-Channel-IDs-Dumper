import discord
import asyncio
import os
import traceback
import logging

TOKEN = 'your-token-here'

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.dm_messages = True

log_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "channel_fetch.log")
logging.basicConfig(
    filename=log_file_path,
    filemode="w",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.DEBUG
)

def log(msg, level=logging.INFO):
    print(msg)
    logging.log(level, msg)

client = discord.Client(self_bot=True, intents=intents)

async def fetch_all_channels():
    try:
        log("\n--- Starting fetch_all_channels ---")
        
        guild_channel_ids = []
        dm_channel_ids = []

        log("Step 1: Fetching DM channels...")
        if not client.private_channels:
            log("No DM channels found.", logging.WARNING)
        else:
            log(f"Total DM channels available: {len(client.private_channels)}")

        for dm_channel in client.private_channels:
            try:
                log(f"Processing DM Channel: {dm_channel} (ID: {dm_channel.id}) | Recipient: {dm_channel.recipient} | Type: {dm_channel.type}")
                dm_channel_ids.append(dm_channel.id)
            except Exception as e:
                log(f"Error processing DM channel {dm_channel}: {e}", logging.ERROR)
                traceback.print_exc()

        log("Step 2: Fetching guild channels...")
        if not client.guilds:
            log("No guilds found.", logging.WARNING)
        else:
            log(f"Total guilds available: {len(client.guilds)}")

        for guild in client.guilds:
            log(f"Processing Guild: {guild.name} (ID: {guild.id})")
            if not guild.channels:
                log(f"No channels found in guild: {guild.name}")
            else:
                log(f"Total channels in {guild.name}: {len(guild.channels)}")

            for channel in guild.channels:
                try:
                    log(f"Processing Guild Channel: {channel} (ID: {channel.id}) | Name: {channel.name} | Type: {channel.type}")
                    guild_channel_ids.append(channel.id)
                except Exception as e:
                    log(f"Error processing guild channel {channel}: {e}", logging.ERROR)
                    traceback.print_exc()

        log("\n--- Channel Summary ---")
        log(f"Total Guild Channel IDs: {len(guild_channel_ids)}")
        log(f"Total DM Channel IDs: {len(dm_channel_ids)}")

        script_dir = os.path.dirname(os.path.abspath(__file__))
        folder_name = os.path.join(script_dir, "Channel-IDs")
        if not os.path.exists(folder_name):
            log(f"Creating folder: {folder_name}")
            os.makedirs(folder_name)
        else:
            log(f"Folder {folder_name} already exists.")

        guild_file_path = os.path.join(folder_name, "guild_channel_ids.txt")
        log(f"Writing guild channel IDs to {guild_file_path}")
        try:
            with open(guild_file_path, "w") as guild_file:
                for guild_id in guild_channel_ids:
                    guild_file.write(f"{guild_id}\n")
            log(f"Successfully wrote guild channel IDs to {guild_file_path}")
        except Exception as e:
            log(f"Error writing guild channel IDs: {e}", logging.ERROR)
            traceback.print_exc()

        dm_file_path = os.path.join(folder_name, "dm_channel_ids.txt")
        log(f"Writing DM channel IDs to {dm_file_path}")
        try:
            with open(dm_file_path, "w") as dm_file:
                for dm_id in dm_channel_ids:
                    dm_file.write(f"{dm_id}\n")
            log(f"Successfully wrote DM channel IDs to {dm_file_path}")
        except Exception as e:
            log(f"Error writing DM channel IDs: {e}", logging.ERROR)
            traceback.print_exc()

        log("Closing the client after fetching all channels.")
        await client.close()

    except Exception as e:
        log(f"Error during fetch_all_channels: {e}", logging.ERROR)
        traceback.print_exc()

@client.event
async def on_ready():
    try:
        log("\n--- on_ready Event ---")
        log(f"Logged in as: {client.user.name} (ID: {client.user.id})")
        log(f"Total Guilds: {len(client.guilds)}")
        log(f"Total Private Channels: {len(client.private_channels)}")
        await fetch_all_channels()
    except Exception as e:
        log(f"Error during on_ready: {e}", logging.ERROR)
        traceback.print_exc()

try:
    log("\n--- Starting the bot ---")
    log(f"Using Token: {TOKEN[:4]}...{TOKEN[-4:]} (token partially hidden for security)")
    client.run(TOKEN, bot=False)
except Exception as e:
    log(f"Error running the client: {e}", logging.ERROR)
    traceback.print_exc()
