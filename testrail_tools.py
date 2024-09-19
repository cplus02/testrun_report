from testrail import APIClient
import yaml

config = yaml.load(open('config.yml'), Loader=yaml.FullLoader)

class TR:
    def __init__(self):
        self.client = APIClient(config['testrail']['base_url'])
        self.client.user = config['testrail']['username']
        self.client.password = config['testrail']['password']

    def get_run_status(self, run_id):
        return self.client.send_get(f"get_run/{run_id}")

    def get_project_runs(self, project_id):
        return self.client.send_get(f"get_runs/{project_id}")

    def get_project_plans(self, project_id):
        return self.client.send_get(f"get_plans/{project_id}")

    def get_plan(self, plan_id):
        return self.client.send_get(f"get_plan/{plan_id}")