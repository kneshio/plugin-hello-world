from waggle.plugin import Plugin
import time

with Plugin() as plugin:
    for i in range(10):
        print("publishing value", i)
        plugin.publish("hello.world.value", i)
        # plugin.publish("my.sensor.name", 123, meta={"camera": "left"})
        # plugin.publish("my.sensor.name", 123, timestamp=my_timestamp_in_ns)
        time.sleep(1)
