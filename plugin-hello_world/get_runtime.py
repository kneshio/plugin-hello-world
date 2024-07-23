from waggle.plugin import Plugin

with Plugin() as plugin:
    # measures duration of input block and publishes to plugin.duration.input
    with plugin.timeit("plugin.duration.input"):
        get_inputs(...)

    # measures duration of inference block and publishes to plugin.duration.inference
    with plugin.timeit("plugin.duration.inference"):
        do_inference(...)

    publish_results(...)