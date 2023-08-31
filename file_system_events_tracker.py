import sys
import time
import random
import os
import shutil

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


from_dir = "/Users/ritvickraghuvanshi/Documents/Python/Project102"

class FileEventHandler(FileSystemEventHandler):
    def on_created(self,event):
        print(f"{event.src_path} has been created")
    def on_deleted(self,event):
        print(f"{event.src_path} has been deleted")
    def on_modified(self,event):
        print(f"{event.src_path} has been modified")
    def on_moved(self,event):
        print(f"{event.src_path} has been moved")   

eventHandler = FileEventHandler()

observe = Observer()

observe.schedule(eventHandler, from_dir, recursive=True)

observe.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped")
    observe.stop()