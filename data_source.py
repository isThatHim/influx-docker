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

    payload = [ 
            { 
                "measurement": "stats", 
                "tags": {
                    "host": "laptop",
                    "metric": "CPU"
                },
                "fields": { 
                    "CPUpercent": currentCPU, 
                }
    
            },
            {
                "measurement": "stats", 
                "tags": {
                    "host": "laptop",
                    "metric": "Memory"
                },
                "fields": {
                    "MEMpercent": currentMemory.percent
                }
            },
            {
                "measurement": "stats", 
                "tags": {
                    "host": "laptop",
                    "metric": "Disk"
                },
                "fields": {
                    "DISKpercent": currentDisk.percent
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
    
