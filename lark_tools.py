import requests
import yaml

config = yaml.load(open('config.yml'), Loader=yaml.FullLoader)

class LarkTools:
    def __init__(self):
        self.base_url = "https://open.larksuite.com/open-apis"
        self.app_id = config['lark']['app_id']
        self.app_secret = config['lark']['app_secret']
        self.tenant_access_token = self._get_tenant_access_token()

    def _get_tenant_access_token(self):
        url = f"{self.base_url}/auth/v3/tenant_access_token/internal/"
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        response = requests.post(url, headers=headers, json=data)
        return response.json()['tenant_access_token']

    def send_message_by_chat_id(self, chat_id, message):
        url = f"{self.base_url}/im/v1/messages?receive_id_type=chat_id"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {self.tenant_access_token}"
        }
        data = {
            "receive_id": chat_id,
            "msg_type": "text",
            "content": f'{{\"text\":\"{message}\"}}'
        }

        print(data)
        response = requests.post(url, headers=headers, json=data)
        return response.json()