import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from_dir = "C:/Users/HP/Downloads"

class FileEventHandler(FileSystemEventHandler):
    
    def on_created(self,event):
        print("Hey, {event.src_path} has been created")
    def on_deleted(self,event):
        print("Oops, someone deleted {event.src_path}")

observer = Observer()
observer.schedule(event_handler,from_dir,recursive = 'True')

event_handler = FileEventHandler()