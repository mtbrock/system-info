import axios from 'axios';
import './styles/index.scss';

function formatBytes(bytes, decimals = 1) {
    if (bytes === 0) return '0 Bytes';

    const k = 1024;
    const dm = decimals < 0 ? 0 : decimals;
    const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];

    const i = Math.floor(Math.log(bytes) / Math.log(k));

    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}

function loadSystemInfo() {
    axios.get('/system-info').then((response) => {
        console.log(response.data);
        const systemData = response.data;

        const cpuValueText = `${systemData.cpu.percent} %`;
        document.getElementById('cpu-value').innerText = cpuValueText;

        const ramValueText = `${systemData.ram.percent} %`;
        const ramTotal = formatBytes(systemData.ram.total);
        const ramUsed = formatBytes(systemData.ram.used);
        document.getElementById('ram-value').innerText = ramValueText;
        document.getElementById('ram-info').innerText = `${ramUsed} / ${ramTotal}`;

        const diskValueText = `${systemData.disk.percent} %`;
        const diskTotal = formatBytes(systemData.disk.total);
        const diskUsed = formatBytes(systemData.disk.used);
        document.getElementById('disk-value').innerText = diskValueText;
        document.getElementById('disk-info').innerText = `${diskUsed} / ${diskTotal}`;
    })
}

window.setInterval(loadSystemInfo, 1000);
