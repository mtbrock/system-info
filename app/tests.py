from django.test import TestCase
from .system_info import SystemInfo

# Create your tests here.
class TestSystemInfo(TestCase):
    def setUp(self):
        self.system_info = SystemInfo()

    def test_cpu_percent(self):
        cpu_percent = self.system_info.get_cpu_percent()

    def test_ram_stats(self):
        ram_stats = self.system_info.get_ram_stats()
        assert ram_stats.percent
        assert ram_stats.available
        assert ram_stats.total
        assert ram_stats.used

    def test_disk_stats(self):
        disk_stats = self.system_info.get_disk_stats()
        assert disk_stats.percent
        assert disk_stats.free
        assert disk_stats.total
        assert disk_stats.used
