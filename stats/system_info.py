import psutil


class SystemInfo:
    def get_cpu_percent(self):
        return psutil.cpu_percent()

    def get_ram_stats(self):
        return psutil.virtual_memory()

    def get_disk_stats(self):
        return psutil.disk_usage('/')
