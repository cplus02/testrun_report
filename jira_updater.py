from jira import JIRA
import yaml

# Read the config file
config = yaml.load(open('config.yml'), Loader=yaml.FullLoader)

class UseJIRA:
    def __init__(self):
        # Sometimes login may fail because of captcha needed to be solved, login to jira in browser and try again, keep password updated
        self.client = JIRA(options={'server': config['jira']['base_url'], 'verify': False}, basic_auth=(config['jira']['username'], config['jira']['password']))