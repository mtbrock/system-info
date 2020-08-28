from django.test import TestCase
from .system_info import SystemInfo


class TestSystemInfo(TestCase):
    def setUp(self):
        self.system_info = SystemInfo()

    def test_cpu_percent(self):
        cpu_percent = self.system_info.get_cpu_percent()
        assert isinstance(cpu_percent, float)

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


class TestViews(TestCase):
    def test_index(self):
        resp = self.client.get('/')
        assert resp.status_code == 200

    def test_system_info(self):
        resp = self.client.get('/system-info/')
        data = resp.json()
        for key in ('cpu', 'ram', 'disk'):
            assert key in data
