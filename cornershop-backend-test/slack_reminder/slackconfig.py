# The Slack app token
OAUTH_TOKEN = 'YOU NEED TO LOAD SLACK APP TOKEN'
# The Slack channel
SLACK_CHANNEL = '#slack-channel'
SLACK_WEBHOOK = 'https://hooks.slack.com/services/XXX/YYY/ZZZ'
HOST_NAME = "http://localhost:8000/"

DEFAULT_OPTIONS = {
    "slack_beat_init_color": "#FFCC2B",
    "slack_broker_connect_color": "#36A64F",
    "slack_broker_disconnect_color": "#D00001",
    "slack_celery_startup_color": "#FFCC2B",
    "slack_celery_shutdown_color": "#660033",
    "slack_task_prerun_color": "#D3D3D3",
    "slack_task_success_color": "#36A64F",
    "slack_task_failure_color": "#D00001",
    "slack_request_timeout": 1,
    "flower_base_url": None,
    "show_celery_hostname": False,
    "show_task_id": True,
    "show_task_execution_time": True,
    "show_task_args": True,
    "show_task_kwargs": True,
    "show_task_exception_info": True,
    "show_task_return_value": True,
    "show_task_prerun": False,
    "show_startup": True,
    "show_shutdown": True,
    "show_beat": True,
    "show_broker": False,
    "use_fixed_width": True,
    "include_tasks": None,
    "exclude_tasks": None,
    "failures_only": False,
    "webhook": True,
    "beat_schedule": None,
    "beat_show_full_task_path": False,
}
