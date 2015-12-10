#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

BASEDIR = os.path.abspath(os.path.dirname('/Users/daihei.doi/Desktop/md_files'))

def getext(filename):
    return os.path.splitext(filename)[-1].lower()

class ChangeHandler(FileSystemEventHandler):

    def on_any_event(self, event):
        if event.is_directory:
            return
        if getext(event.src_path) in ('.md'):
		#param = os.path.basename(event.src_path)		
       		#os.system('python ~/Desktop/Bayashin/slack_pythons/slack_test_post.py ' + param)
		print(event)

    def on_created(self, event):
        if event.is_directory:
            return
        if getext(event.src_path) in ('.md'):
		param = os.path.basename(event.src_path)
		state = '作成した'		
       		os.system('python ~/Desktop/Bayashin/slack_pythons/slack_test_post.py ' + param + ' ' + state )

    def on_modified(self, event):
        if event.is_directory:
            return
        if getext(event.src_path) in ('.md'):
            	param = os.path.basename(event.src_path)		
		state = '更新した'		
       		os.system('python ~/Desktop/Bayashin/slack_pythons/slack_test_post.py ' + param + ' ' + state )

    def on_deleted(self, event):
        if event.is_directory:
            return
        if getext(event.src_path) in ('.md'):
            	param = os.path.basename(event.src_path)		
		state = '削除した'		
       		os.system('python ~/Desktop/Bayashin/slack_pythons/slack_test_post.py ' + param + ' ' + state )

if __name__ in '__main__':
    while 1:
        event_handler = ChangeHandler()
        observer = Observer()
        observer.schedule(event_handler,BASEDIR,recursive=True)
        observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()
