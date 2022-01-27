import os
import time
import requests
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import watchdog

# from config import discord_webhook_url, bot_name, path
import config


class MyHandler(PatternMatchingEventHandler):
    def __init__(self, command, patterns):
        super(MyHandler, self).__init__(patterns=patterns)
        self.command = command

    def _run_command(self, event):
        self.command(event)

    def on_moved(self, event):
        # self._run_command()
        pass

    def on_created(self, event):
        # print(event)
        self._run_command(event)

    def on_deleted(self, event):
        # self._run_command()
        pass

    def on_modified(self, event):
        # self._run_command()
        pass


def watch(path, command, patterns):
    event_handler = MyHandler(command, patterns)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


def discord_webhook(webhook_url, message, name):
    content = {
        "content": message,
        "username": name,
    }
    requests.post(webhook_url, content)


def action(event):
    filename = os.path.basename(event.src_path)
    timestr = time.strftime("%Y-%m-%d %H:%M:%S")
    message = f"create {filename} {timestr}"
    print(message)
    # webhookを叩いたりする
    discord_webhook(config.discord_webhook_url, message, config.bot_name)


if __name__ == "__main__":
    path = config.path

    print("start")
    watch(path, action, config.match_patterns)
