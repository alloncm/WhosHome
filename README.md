# WhosHome?

WhosHome is a telegram bot you can run on your local home network in order to get an answer to the question "Who's Home?" whenever you want.

The bot does this by using `nmap` and parsing its output.

**Disclaimer**

I didn't find a python library that wrap `nmap` and will allow me complete control on the nmap command so I just parsed nmap output (I know its ugly and if someone has another option I will be happy to hear :)).

This script currently works only on linux and the user running it should have `sudo` preveliges.

## How to spy on my family too?

The script has a `config.py` file, please edit it and add the neccessary details there.
The script require a bit of investigation activity in order to fill the mapping table between mac address and home member.

### installation

The script needs to run on a unix machine connected to the home network.

Steps:
* Install nmap - `sudo apt-get install nmap`

* Register a bot at telegram using the [BotFather](https://core.telegram.org/bots#6-botfather)

* Clone the repo

* Fill the missing details in the `config.py` file
    * Enter the telegram bot token received when creating your bot.
    * The host password (you can read the code it will use it to run nmap with sudo).
    * Ip range to scan, example 1.1.1.0-255 will scan for all the ip addresses from 1.1.1.0 to 1.1.1.255.
    * The mapping between a mac address and a member name.
    * List of allowed ids - every telegram message will have the user id with it, you can receive it by sending a message to the `Telegram Raw Bot`.

* Install deps - `pip install -r requirements.txt`

* Optinal: tell the family about the bot and register them as valid members :)

**Another disclaimer**

This one of my first python programs so Ill gladly take any advices and pull requests!