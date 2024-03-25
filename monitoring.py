from datetime import datetime
import time
import psutil
import logging
from opensearchpy import OpenSearch
from Consts import LOG_FILE, SERVICES, INTERVAL_SECS, TIMEOUT_SECS
log = logging.getLogger(__name__)

# Connect to OpenSearch
opensearch = OpenSearch([{'host': 'localhost', 'port': 9200}])

logging.basicConfig(filename=LOG_FILE,
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s '
                           '%(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO)


# Retrieve specific running services
def collect_os_services_data(services):
    for proc in psutil.process_iter(['name', 'memory_info', 'memory_percent', 'cpu_percent']):
        if proc.name() in services:
            # Get CPU usage as a percentage
            cpu_percent = proc.info['cpu_percent']
            # Get memory usage in bytes
            memory_info = proc.info['memory_info']
            # Get Memory usage as a percentage
            memory_percent = proc.info['memory_percent']
            memory_usage = memory_info.rss  # Resident Set Size (RSS)
            # Convert memory usage to megabytes
            memory_usage_mb = memory_usage / (1024 * 1024)
            log.info(proc)
            # send  service cpu,memory usage to openSearch system
            service_data = {'timestamp': str(datetime.utcnow()),
                            'service_name': proc.name(),
                            'cpu_percent': cpu_percent,
                            'memory_percent': memory_percent,
                            'memory_usage_mb': memory_usage_mb}
            opensearch.index(index=proc.name(), body=service_data)
            log.info(service_data)


# Retrieve main metrics of Operating system : Cpu,memory,disk, networking
def collect_os_metrics():
    total_cpu = psutil.cpu_percent(interval=1)
    total_memory = psutil.virtual_memory().percent
    disk_percent = psutil.disk_usage('/').percent
    network_bytes_sent = psutil.net_io_counters().bytes_sent
    network_bytes_recv = psutil.net_io_counters().bytes_recv
    # send OS system metrics usage to openSearch system
    os_system_data = {'timestamp': str(datetime.utcnow()),
                      'total_cpu': total_cpu,
                      'total_memory': total_memory,
                      'disk_percent': disk_percent,
                      'network_bytes_sent': network_bytes_sent,
                      'network_bytes_recv': network_bytes_recv
                      }
    log.info(os_system_data)
    opensearch.index(index='laptop_performance', body=os_system_data)


if __name__ == '__main__':
    end_time = time.time() + TIMEOUT_SECS
    while time.time() <= end_time:
        collect_os_services_data(services=SERVICES)
        collect_os_metrics()
        time.sleep(INTERVAL_SECS)
