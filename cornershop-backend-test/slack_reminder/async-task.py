import json
from datetime import datetime

from celery.app.trace import logger
from celery.worker.state import requests

from option.models import Option
from backend_test.celery import app


# https://github.com/crflynn/celery-slack
from slack_reminder.slackconfig import HOST_NAME, SLACK_WEBHOOK


@app.task(bind=True, default_retry_delay=10 * 60)
def options_menu_send_reminder():
    """
    Send a reminder to an Slack channel with the Menu of the day
    """
    try:
        today = datetime.today().strftime("%Y-%m-%d")
        options = Option.objects.filter(published_date=today)
        options_text = ""
        uuid = ""
        for idx, option in options:
            options_text += str(idx)+" " + option.description + " " + "\n"
            uuid = option.menu_uuid
        menu_url = HOST_NAME + 'menu/' + uuid
        text = f"I Share with you  today's menu! <{menu_url}|Click here> for details!"
        text += options_text
        payload = {"text": text}
        response = requests.post(SLACK_WEBHOOK, data=json.dumps(payload))

        logger.info('Async task message status=%s', response.status_code)
    except Option.DoesNotExist:
        logger.error('Async task error message status=failed')
