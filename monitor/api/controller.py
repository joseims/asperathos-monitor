from monitor.plugins.spark_progress import SparkProgress


class Controller:

    def __init__(self):
        self.app_monitored = {}

    def start_monitor(self, plugin_name, info_plugin, collect_period):
        print "Starting monitoring..."
        plugin = None

        if info_plugin['spark_id'] not in self.app_monitored:
            if plugin_name == "spark_progress":
                plugin = SparkProgress(info_plugin, collect_period)
                self.app_monitored[info_plugin['spark_id']] = plugin

            print "Starting plugin: %s" % plugin.getName()
            plugin.start()

        else:
            print "The application  is already being monitored"

    def kill_monitor(self, app_id):
        try:
            self.app_monitored.pop(app_id, None).stop()
        except Exception as ex:
            ex.message
            pass

