from waggle.plugin import Plugin
from waggle.data.audio import Microphone
import time

with Plugin() as plugin, Microphone() as microphone:
    # record and upload a 10s sample periodically
    while True:
        sample = microphone.record(10)
        sample.save("sample.ogg")
        plugin.upload_file("sample.ogg")
        time.sleep(300)