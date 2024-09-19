import pygsheets
import pandas as pd
import yaml

config = yaml.load(open('config.yml'), Loader=yaml.FullLoader)

class GSheetTools:
    def __init__(self, url):
        self.gc = pygsheets.authorize(service_file=f'./{config["gsheet"]["credentials"]}')
        self.spreadsheet = self.gc.open_by_url(url)

    def get_all_test_run_id(self, team_name):
        worksheet =  self.spreadsheet.worksheet_by_title(team_name)
        if worksheet is None:
            print("No worksheet found")
            return

        df = worksheet.get_as_df()
        return df["Test_run_number"].tolist()