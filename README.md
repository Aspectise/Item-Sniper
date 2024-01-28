# Item-Sniper
Item Sniper snipes regular roblox UGC and non UGC items, this sniper can not snipe ugc limited if you want a ugc limited visit [Limited Sniper](https://github.com/Aspectise/Limited-Sniper):

## Setup
```json
{
    "Webhook": {
        "Enabled": false, If true will send a notification to the webhook url you added
        "Url": "" If you set enabled to true you have to add a webhook url here
    },
    "Buy_cookies": [
        "" Your roblox account cookie that will buy the items (main account cookie)
    ],
    "Check_cookie": "", Your roblox alt account cookie that will check the ids (can be the same as buy cookie)

    "Items": {
        "553722174": 2, Ids with expected price
        "417457139": 5
    },

    "Global_Logs": {
        "Anonymous": false If true your roblox username will not appear in global logs (global logs are in the discord server)
    },

    "Discord": {
        "Enabled": false, Put to true if you want to manage the sniper using discord commands
        "Token": "", If you made Enabled to true you have to add a discord bot token here
        "Owner_id": [] Put the discord user ids of people that are allowed to use the commands of the bot
    }
}
```

<details>
<summary><strong>How to get discord token! (Click to expand) </strong></summary>

    
#### Create a new [application](https://discord.com/developers/applications)

![image](https://github.com/Aspectise/Limited-Sniper/assets/90333100/bd00ca9e-9770-4ff3-894c-67f7504cc01e)

#### Enable these 3 intents

![image](https://github.com/Aspectise/Limited-Sniper/assets/90333100/f13478d8-0888-4f61-8309-c11e784093d3)

#### Get the token by clicking copy

![image](https://github.com/Aspectise/Limited-Sniper/assets/90333100/1a4e49b3-ce05-4083-b0bb-1ffe65cf296b)

#### To invite the bot: Click copy and paste the url in your browser

![image](https://github.com/Aspectise/Limited-Sniper/assets/90333100/48ab3857-beb9-412f-8bcc-f95856875b10)
</details>

# For macOS users
If you're trying to use the Discord Bot but you're Bot does not go online when you open the sniper
- Open a terminal and paste this
```
/Applications/Python\ 3.11/Install\ Certificates.command
```

### Features:
- [x] - **Checks ids at fast speed**
- [x] - **4 watchers implemented**
- [x] - **Supports Multi-ID**
- [x] - **Webhook Support** 
- [x] - **Can be ran in AWS** 
- [x] - **Snipes every Item except Limiteds** 
- [x] - **Discord Bot w/ Slash Commands** 

## Preview:
![image](https://github.com/Aspectise/Item-Sniper/assets/90333100/eca47999-3dd7-4167-92df-9a83c82089c2)

## IMPORTANT!
- If you don't trust it don't use it. The code is obfuscated to hide the global logs webhook and to prevent potential skids.
- If main.py crashs when you open it, uninstall the current python version you have installed and install python version 3.11.x
## Help
If you need help setting up the bot join the [Discord](https://discord.gg/deathsniper)
