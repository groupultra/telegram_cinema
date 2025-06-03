# Telegram Cinema

## Project Introduction

Telegram Cinema is a Python-based Telegram bot designed to orchestrate group conversations according to a predefined script. By leveraging multiple Telegram accounts, the bot can simulate natural, multi-person dialogues in group chats, making it ideal for scenarios such as:
- **Scripted Role-Playing**: Automatically play out stories, debates, or educational scenarios in a group, with each bot account representing a different character.
- **Demo & Training**: Showcase group chat features, moderation, or onboarding flows in a controlled, repeatable way.
- **Interactive Storytelling**: Bring stories to life in chat groups, where each message is sent by a different character at scheduled times.

In addition to its core script-driven conversation feature, Telegram Cinema also supports basic bot message responses and can be easily extended for custom group automation needs.

## Quick Start

### 1. Clone the Repository

```bash
git clone git@github.com:groupultra/telegram_cinema.git
cd telegram_cinema
```

### 2. Install Dependencies

This project requires Python 3. Please make sure you have Python 3 installed.

```bash
pip install telethon
```

Amazing! There is only one dependency, `telethon`!

### 3. Configure Account Information

Copy the example configuration file and fill in your Telegram Bot Token and other required information:

```bash
cp accounts.json.example accounts.json
cp .env.example .env
```

Edit `accounts.json` and provide your account details.

Edit `.env` and provide your API ID and API Hash.

### 4. Run the Project

```bash
python main.py
```

### 5. Additional Notes

- You can modify `story_talker.py`, `event_handler.py`, and other files to extend the bot's functionality.
- To add custom scripts, use the `scripts/` directory.

## Contribution

Feel free to submit issues and pull requests to help improve this project!
