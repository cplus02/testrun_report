from testrail_updater import TR
from jira_updater import UseJIRA
def test():
    a = TR()
    run_info = a.get_run_status("139")

    b = UseJIRA()

    print(run_info)

if __name__ == "__main__":
    test()