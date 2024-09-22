Language Translator Discord Bot

This is a multilingual translation Discord bot built with Python. The bot automatically translates messages between users in a Discord server based on their preferred languages, and supports manual translations upon request.
## Features
- Automatically translates messages to the preferred language of each user.
- Users can set their preferred language.
- Translates text on command.
- Supports all languages available through Google Translate API.

## Tech Stack
- Python
- Discord API wrapper for Python
- Googletrans(Python API for Google Translate)
- [python-dotenv] (for managing environment variables)

## Prerequisites

Ensure you have the following installed on your machine:

- [Python 3.8+](https://www.python.org/downloads/)
- `pip` (Python package manager)
- A Discord account and server to invite the bot

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Language-Translator-Discord-Bot.git
cd Language-Translator-Discord-Bot


2. Install dependencies

pip install -r requirements.txt

The requirements.txt file should contain:

discord.py
googletrans==4.0.0-rc1
python-dotenv
3. Create and set up the .env file
Create a .env file in the root of your project directory and add the following:
bash
Copy code
DISCORD_BOT_TOKEN=your_discord_bot_token_here
Replace your_discord_bot_token_here with your actual Discord bot token (keep it secure and don't share it publicly).
4. Run the bot
After setting everything up, you can run the bot using:
bash
Copy code
python bot.py

Usage
Commands
Set Language: Set your preferred language using the command:
bash
Copy code
!setlanguage <language_code>

Example: !setlanguage en will set your preferred language to English.
Translate: Translate a specific message manually with the !translate command:
bash
Copy code
!translate <language_code> <message>

Example: !translate fr Hello, how are you? will translate the text into French.
Supported Languages
This bot supports all languages offered by the Google Translate API. You can view the full list of language codes here.



