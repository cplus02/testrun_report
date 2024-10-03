from testrail_tools import TR
from gsheet_tools import GSheetTools
from telegram import Bot
from lark_tools import LarkTools
import sys
import asyncio
import yaml


config = yaml.load(open('config.yml'), Loader=yaml.FullLoader)

async def send_report():
    tr = TR()
    gs = GSheetTools(config['gsheet']['qa_report_url'])
    bot = Bot(token=config['telegram']['token'])
    chat_id = config['telegram']['channel_id']
    lk = LarkTools()

    # System argument 1 is the team name
    team_name = sys.argv[1]
    run_ids = gs.get_all_test_run_id(team_name)

    await bot.send_message(chat_id, f"The following is {team_name} team all test run status", parse_mode='markdown')

    for run_id in run_ids:
        run_info = tr.get_run_status(run_id)
        await bot.send_message(chat_id, format_report(run_info, "telegram"), parse_mode='Markdown')
        lk.send_message_by_chat_id(config['lark']['group_id'], format_report(run_info, "lark"))

def format_report(run_info, im_type):
    report = ''

    # Format the report
    run_title = run_info['name']
    run_passed = run_info['passed_count']
    run_failed = run_info['failed_count']
    run_blocked = run_info['blocked_count']
    run_untested = run_info['untested_count']
    run_retest = run_info['retest_count']
    run_not_implemented = run_info['custom_status1_count']
    run_not_available = run_info['custom_status2_count']
    run_testing = run_info['custom_status3_count']
    run_url = run_info['url']

    total_cases = run_passed + run_failed + run_blocked + run_untested + run_retest + run_not_implemented + run_not_available + run_testing

    # Passed rate 取到整數
    passed_rate = int(run_passed / total_cases * 100)
    # Format as markdown v1 for telegram
    # Long version
    # report = f"*{run_title}*\n\n*PASSED*: {run_passed}\n*FAILED*: {run_failed}\n*BLOCKED*: {run_blocked}\n*UNTESTED*: {run_untested}\n*RETEST*: {run_retest}\n*NOT IMPLEMENTED*: {run_not_implemented}\n*NOT AVAILABLE*: {run_not_available}\n*TESTING*: {run_testing}\n\n*PASSED RATE*: {passed_rate}%\n\n{run_url}"

    # Short version
    if im_type == 'telegram':
        report = f"*{run_title}*\n\n*PASSED*: {run_passed}\n*FAILED*: {run_failed}\n*BLOCKED*: {run_blocked}\n*UNTESTED*: {run_untested}\n*RETEST*: {run_retest}\n\n*PASSED RATE*: {passed_rate}%\n\n{run_url}"
    elif im_type == 'lark':
        report = f"<b>{run_title}</b>\\n\\n<b>PASSED</b>: {run_passed}\\n<b>FAILED</b>: {run_failed}\\n<b>BLOCKED</b>: {run_blocked}\\n<b>UNTESTED</b>: {run_untested}\\n<b>RETEST</b>: {run_retest}\\n\\n<b>PASSED RATE</b>*: {passed_rate}%\\n\\n{run_url}"

    return report



if __name__ == "__main__":
    asyncio.run(send_report())