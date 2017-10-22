""" Wrapper under requests to the BOTAN"""
import os
import requests


class Botan():
    """ Class for send statistics into APP Metrica"""
    def __init__(self, token):
        self.token = token
        self.track_url = 'https://api.botan.io/track'
        self.is_enabled = "DEBUG" not in os.environ

    def send_stats(self, message):
        """ Sends statictics"""
        if self.is_enabled:
            try:
                uid = message.from_user.id
                self.__track(uid, message, 'Show')
            except:
                print("Stats send failure")

    def __make_json(self, message):
        """ Convert telegram message data to json"""
        data = {}
        data['message_id'] = message.message_id
        data['from'] = {}
        data['from']['id'] = message.from_user.id
        if message.from_user.username is not None:
            data['from']['username'] = message.from_user.username
        data['chat'] = {}

        data['chat']['id'] = message.chat.id
        return data

    def __track(self, uid, message, name='Message'):
        """ Send message """
        try:
            request = requests.post(
                self.track_url,
                params={"token": self.token, "uid": uid, "name": name},
                data=self.__make_json(message),
                headers={'Content-type': 'application/json'},
            )
            return request.json()
        except requests.exceptions.Timeout:
            # set up for a retry, or continue in a retry loop
            return False
        except (requests.exceptions.RequestException, ValueError) as e:
            # catastrophic error
            print(e)
            return False
