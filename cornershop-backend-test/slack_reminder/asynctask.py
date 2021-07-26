import json
from datetime import datetime

from celery.app.trace import logger
import requests
from django.core.serializers import serialize

from option.models import Option
from backend_test.celery import app

# https://github.com/crflynn/celery-slack
from slack_reminder.slackconfig import HOST_NAME, SLACK_WEBHOOK


@app.task(bind=True)
def options_menu_send_reminder(self, request):
    """
    Send a reminder to an Slack channel with the Menu of the day
    """
    try:
        today = datetime.today().strftime("%Y-%m-%d")
        options = Option.objects.filter(publish_date=today)
        menu_options = serialize("json", options)

        options_text = ""
        uuid = ""

        json_dictionary = json.loads(menu_options)
        print(json_dictionary)
        for option in json_dictionary:
            print(option["fields"]["description"])
            options_text += option["fields"]["description"] + " " + '\n' + " "
            uuid = option["fields"]["menu_uuid"]
        menu_url = HOST_NAME + 'menu/' + uuid
        text = f"I Share with you  today's menu! <{menu_url}> click for details!"

        payload = {"text": "{} {}".format(text, options_text)}
        print(payload)
        response = requests.post(SLACK_WEBHOOK, data=json.dumps(payload))

        logger.info('Async task message status=%s', response.status_code)
    except Exception as error:
        logger.error('Async task error message status=failed')
