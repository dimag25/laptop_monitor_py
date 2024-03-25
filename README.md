## Measure and characterize the performance and resources consumption of my laptop.



### COLLECTED DATA:
  - Specific Services memory/cpu usage ( `SERVICES` List in `Consts.py` )
    It is important to limit to specific services measure ,
    to prevent heavy usage of all running services check, 
    most important metrics are cpu and memory per service.

  - OS System Important Metrics:
      - CPU usage: Check total cpu usage.
      - Memory usage: Total memory and memory usage percentage.
      - Disk usage: Total disk space and disk usage percentage.
      - Network activity: Bytes sent and received.

## Project Setup


### Step 1: Clone the project

```bash
git clone https://github.com/dimag25/laptop_monitor_py.git
cd laptop_monitor_py
```

### Step 2 : need to make sure opensearch installed & running on your machine.
- Windows : https://opensearch.org/docs/latest/install-and-configure/install-opensearch/windows/
- For other OS(mac/linux) check docs : https://opensearch.org/docs/latest/install-and-configure/install-opensearch/index/
- install requirements.txt libs: 
```bash
pip install -r requirements.txt
```

### Step 3: `Run locally from any OS ( Win/Mac/Linux )`
- Local Run Monitoring tool:
(Runs for 60 secs with 5 secs intervals)

```bash 
  python3 monitoring.py
```


### Note: 
SERVICES in Consts.py - example  for Windows OS.


### Output example :
```bash 
  python3 test_results.py
```

```
[laptop_performance]: {'timestamp': '2024-03-25 14:10:01.297222', 'total_cpu': 26.9, 'total_memory': 93.8}
[laptop_performance]: {'timestamp': '2024-03-25 14:11:40.433905', 'total_cpu': 51.5, 'total_memory': 94.6}
[laptop_performance]: {'timestamp': '2024-03-25 14:13:20.123548', 'total_cpu': 28.9, 'total_memory': 93.2}
[laptop_performance]: {'timestamp': '2024-03-25 14:13:58.728128', 'total_cpu': 25.7, 'total_memory': 93.9}
[laptop_performance]: {'timestamp': '2024-03-25 14:26:39.743977', 'total_cpu': 46.6, 'total_memory': 92.1, 'disk_percent': 40.9, 'network_bytes_sent': 420231264, 'network_bytes_recv': 3448580572}
[laptop_performance]: {'timestamp': '2024-03-25 14:26:52.159067', 'total_cpu': 85.7, 'total_memory': 90.2, 'disk_percent': 40.9, 'network_bytes_sent': 420838209, 'network_bytes_recv': 3448613300}
[laptop_performance]: {'timestamp': '2024-03-25 14:27:03.640813', 'total_cpu': 83.8, 'total_memory': 91.8, 'disk_percent': 40.9, 'network_bytes_sent': 420885118, 'network_bytes_recv': 3448675105}
[laptop_performance]: {'timestamp': '2024-03-25 14:27:15.580165', 'total_cpu': 57.3, 'total_memory': 91.2, 'disk_percent': 40.9, 'network_bytes_sent': 420896953, 'network_bytes_recv': 3448697912}
[laptop_performance]: {'timestamp': '2024-03-25 14:27:25.358367', 'total_cpu': 71.7, 'total_memory': 85.9, 'disk_percent': 40.9, 'network_bytes_sent': 420967224, 'network_bytes_recv': 3448864473}
[laptop_performance]: {'timestamp': '2024-03-25 14:27:36.899882', 'total_cpu': 44.4, 'total_memory': 86.0, 'disk_percent': 40.9, 'network_bytes_sent': 421080930, 'network_bytes_recv': 3449489668}
[chrome.exe]: {'timestamp': '2024-03-25 14:35:07.746154', 'service_name': 'chrome.exe', 'cpu_percent': 2.8, 'memory_percent': 1.6962903801647746, 'memory_usage_mb': 136.2265625}
[chrome.exe]: {'timestamp': '2024-03-25 14:35:08.807056', 'service_name': 'chrome.exe', 'cpu_percent': 0.1, 'memory_percent': 0.26436136423110485, 'memory_usage_mb': 21.23046875}
[chrome.exe]: {'timestamp': '2024-03-25 14:35:08.840723', 'service_name': 'chrome.exe', 'cpu_percent': 0.1, 'memory_percent': 0.46446856799315916, 'memory_usage_mb': 37.30078125}
[chrome.exe]: {'timestamp': '2024-03-25 14:35:09.096886', 'service_name': 'chrome.exe', 'cpu_percent': 0.1, 'memory_percent': 0.42750175349166153, 'memory_usage_mb': 34.33203125}
[chrome.exe]: {'timestamp': '2024-03-25 14:35:19.958795', 'service_name': 'chrome.exe', 'cpu_percent': 3.3, 'memory_percent': 1.7434230686541843, 'memory_usage_mb': 140.01171875}
[chrome.exe]: {'timestamp': '2024-03-25 14:35:20.058934', 'service_name': 'chrome.exe', 'cpu_percent': 0.1, 'memory_percent': 0.24203535389401612, 'memory_usage_mb': 19.4375}
[chrome.exe]: {'timestamp': '2024-03-25 14:35:20.180685', 'service_name': 'chrome.exe', 'cpu_percent': 0.5, 'memory_percent': 0.2895085262012026, 'memory_usage_mb': 23.25}
[chrome.exe]: {'timestamp': '2024-03-25 14:35:20.218083', 'service_name': 'chrome.exe', 'cpu_percent': 0.5, 'memory_percent': 0.6489621566828705, 'memory_usage_mb': 52.1171875}
[chrome.exe]: {'timestamp': '2024-03-25 14:35:20.250249', 'service_name': 'chrome.exe', 'cpu_percent': 0.1, 'memory_percent': 0.46811660889791223, 'memory_usage_mb': 37.59375}
[chrome.exe]: {'timestamp': '2024-03-25 14:35:30.024156', 'service_name': 'chrome.exe', 'cpu_percent': 14.7, 'memory_percent': 1.942314258781321, 'memory_usage_mb': 155.984375}
[python.exe]: {'timestamp': '2024-03-25 14:35:09.160237', 'service_name': 'python.exe', 'cpu_percent': 29.6, 'memory_percent': 0.37779111609622656, 'memory_usage_mb': 30.33984375}
[python.exe]: {'timestamp': '2024-03-25 14:35:20.434147', 'service_name': 'python.exe', 'cpu_percent': 32.8, 'memory_percent': 0.3722947344663986, 'memory_usage_mb': 29.8984375}
[python.exe]: {'timestamp': '2024-03-25 14:35:31.966696', 'service_name': 'python.exe', 'cpu_percent': 33.5, 'memory_percent': 0.372732499374969, 'memory_usage_mb': 29.93359375}
[python.exe]: {'timestamp': '2024-03-25 14:35:46.916719', 'service_name': 'python.exe', 'cpu_percent': 32.8, 'memory_percent': 0.37900712973114425, 'memory_usage_mb': 30.4375}
```

### Logs attached
File : `monitoring_logs.log`

Enjoy! :)
