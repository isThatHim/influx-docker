#!/usr/bin/env python3

import psutil
from influxdb import InfluxDBClient
import time

client = InfluxDBClient(host = 'localhost', port = 8086)
client.switch_database('mdt')

while True:
    currentCPU = psutil.cpu_percent()
    currentMemory = psutil.virtual_memory()
    currentDisk = psutil.disk_usage('/')
    currentDiskIO = psutil.disk_io_counters()
    currentNetworkIO = psutil.net_io_counters()

    payload = [ 
            { 
                "measurement": "stats", 
                "tags": {
                    "host": "NUC",
                    "metric": "CPU"
                },
                "fields": { 
                    "CPUpercent": currentCPU, 
                }
    
            },
            {
                "measurement": "stats", 
                "tags": {
                    "host": "NUC",
                    "metric": "Memory"
                },
                "fields": {
                    "MEMpercent": currentMemory.percent
                }
            },
            {
                "measurement": "stats", 
                "tags": {
                    "host": "NUC",
                    "metric": "Disk"
                },
                "fields": {
                    "DISKpercent": currentDisk.percent
                }
            },
            {
                "measurement": "stats", 
                "tags": {
                    "host": "NUC",
                    "metric": "Disk"
                },
                "fields": {
                    "DISKread": currentDiskIO.read_bytes
                }
            },
            {
                "measurement": "stats", 
                "tags": {
                    "host": "NUC",
                    "metric": "Disk"
                },
                "fields": {
                    "DISKwrite": currentDiskIO.write_bytes
                }
            },
            {
                "measurement": "stats", 
                "tags": {
                    "host": "NUC",
                    "metric": "Network"
                },
                "fields": {
                    "NETrecv": currentNetworkIO.bytes_recv
                }
            },
            {
                "measurement": "stats", 
                "tags": {
                    "host": "NUC",
                    "metric": "Network"
                },
                "fields": {
                    "NETsent": currentNetworkIO.bytes_sent
                }
            }
    ]
    
    response = client.write_points(payload)
    print("Payload:", payload)
    print("Response:", response)
    print("------------------------")
    
    #results = client.query('SELECT "CPUpercent" FROM "mdt"."autogen"."stats" WHERE time > now() - 10s')
    #print("Results", results.raw)
    #print(">-----------------------<")

    time.sleep(5)
    
