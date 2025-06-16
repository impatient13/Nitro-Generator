# Discord Nitro Generator & Checker

This Python script generates random Discord Nitro gift codes (normal or promo), verifies their validity through the official Discord API, and reports the results in the console with color-coded output. Valid codes are saved locally and can be sent to a Discord webhook.

---

## Features

- Generates random Discord Nitro codes:
  - Normal Nitro (16-character codes)
  - Promo Nitro (24-character codes)
- Validates codes by querying Discord's API
- Color-coded console output (valid in green, invalid in red)
- Saves valid codes automatically to `valids.txt`
- Optionally sends valid codes to a Discord webhook
- Simple user interface in the terminal

SCREEN:

![image](https://github.com/user-attachments/assets/ee263a6d-1a8d-4a7d-b11a-fe9f3bdf3ee7)

---

## Requirements

- Python 3.6+
- Required Python packages:
  - `requests`
  - `colorama`

Install dependencies via:

```bash
pip install requests colorama
