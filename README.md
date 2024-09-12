# Discord Channel IDs Dumper

## Overview
`Discord Channel IDs Dumper` is designed to fetch and dump all channel IDs from a user's Discord account. This includes both direct message (DM) channels and guild (server) channels, as well as organizes the retrieved channel IDs into separate text files, providing a straightforward way to collect channel IDs for various purposes.

Obviously using Discord's API and doesn't require any permissions for channel fetching (even private channels), as it utilizes the account's inherent access.

## Features
- Fetches all Direct Message (DM) and guild channels.
- Saves channel IDs into organized text files.
- Automatically creates necessary directories to store the output files.
- Detailed logging for debugging and audit purposes.
- Easy-to-understand output and error handling.

## Requirements
- Python 3.7+
- `discord.py v1.6.0` (due to selfbot functionality)
- A Discord token (selfbot)

### Discord API Permissions
No permissions are required to run this, works with any user account's default access permissions and doesm't require additional scopes, as it simply reads accessible data (channel IDs).

> **Note:** Selfbots are against Discord’s Terms of Service. Use this script responsibly, and be aware of the risks associated with selfbot usage, including account suspension or banning.

## Installation

### Step 1: Clone the repository
```bash
git clone https://github.com/YaBoiSwayZ/Discord-Channel-IDs-Dumper.git
cd Discord-Channel-IDs-Dumper-Main
```

### Step 2: Install dependencies
Ensure you have `discord.py` installed (version `1.6.0` is required for selfbot support).
```bash
pip install discord.py==1.6.0
```

### Step 3: Configure the script
- Open the script and replace the placeholder token (`TOKEN = 'your-token-here'`) with your actual Discord token.

## Usage

To run the script, follow these steps:

1. **Run the Python Script:**
   ```bash
   python Dump.py
   ```

2. **Fetch Results:**
   The script will fetch all DM and guild channels and log the results in a newly created folder called `Channel-IDs`, with two text files:
   - `guild_channel_ids.txt` (for server channels)
   - `dm_channel_ids.txt` (for direct message channels)

### Example
The output folder will be created in the same directory as the script:
```
Channel-IDs/
    ├── guild_channel_ids.txt
    └── dm_channel_ids.txt
```

## Interaction with Discord API
 Again, uses Discord's API through the `discord.py` library to fetch the following data:
- **Direct Messages (DM) Channels**: Every private conversation the user has, including any open DM channels.
- **Guild Channels**: All channels from every server (guild) the user is part of.

### Key API Calls
- **Fetching DM Channels**: Utilizes `client.private_channels` to retrieve all active DM channels.
- **Fetching Guilds**: Uses `client.guilds` to retrieve a list of all servers the user is in, followed by fetching `guild.channels` for channel-specific data.

## Troubleshooting

### Common Issues and Solutions

- **Bot Fails to Login:**
  Make sure the token provided is correct. Tokens are case-sensitive and shouldn't have any leading or trailing spaces.
  - *Error*: `401 Unauthorized`
  - *Solution*: Check if the token has expired or is invalid.

- **Stuck After Fetching DMs:**
  The script may seem to hang after fetching DM channels. This might be due to rate-limiting issues when fetching a large number of guild channels.
  - *Solution*: Make sure the account has a reasonable number of servers and channels, 200 servers is the cap but channels weithin those servers are a different story.

- **Rate Limiting:**
  If you are part of many large servers, the API may start throttling requests.
  - *Solution*: Add a `await asyncio.sleep()` delay between API calls if rate-limiting becomes an issue.

- **Error When Writing to Files:**
  Ensure that you have write permissions to the directory where the script is located.
  - *Error*: `PermissionError`
  - *Solution*: Check directory permissions or run the script as an administrator.

## Do Me A Favour By Contributing
We welcome contributions from the community! To contribute:

1. Fork this repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes with clear descriptions.
4. Open a pull request to this repository.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Disclaimer
This script uses a selfbot which is against Discord's Terms of Service. Use at your own risk, and be aware of potential repercussions like account suspension or ban.
