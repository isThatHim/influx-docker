# influx-docker
InfluxDB + Telgraf + Kapacitor + Chronograf + Grafana for System Monitoring

This repository contains a docker-compose file to bring up an integrated
Influxdata InfluxDB, Telgraf, Chronograf, Kapacitor, and Grafana stack. It is
provided with a Python script (data_source.py) which can be run as an example
to produce test data in the database using metrics from the local machine.
Telegraf is also configured to collect various metrics from a Synology NAS
using the Synology SNMP MIBs.

## Usage

### Requirements
This system requires Docker, Python 3 and Python modules in the included
requirements.txt. To install the Python modules, use:
```
$ pip install -r requirements.txt
```

It also requires you to download and install the required SNMP MIBs to the
data/mibs directory. Apologies, but Synology SNMP MIBs are Copyright, so we 
cannot include them in this GitHub repository.

To download the Synology MIB file, go to:
https://global.download.synology.com/download/Document/MIBGuide/Synology_MIB_File.zip

Simply unzip the Synology_MIB_File.zip, placing all the resulting files in the data/mibs directory.

### Running
```
$ docker-compose up
```

will start the components. 

You will need to create the databases in InfluxDB in order to store time-series
values for the various metrics. The configuration currently uses two databases,
one for telemetry data and one for Synology SNMP data.

```
$ curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE mdt"
$ curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE synology"
```

You may now execute the test script. This is only required in order to put some
example data in the mdt database from the host Linux system:

```
$ python data_source.py
```

This will run every 5 seconds inserting CPU and Memory usage stats from the
local machine in to the new InfluxDB database.

You may now open a Web browser and go to 'localhost:3000', username admin,
password admin, to access Grafana. Here, navigate to the Dashboard tab, and
_import_ a dashboard. Browse to the local directory and import the sample JSON
file provided (CPU-and-Memory.json). This dashboard should load and start to
provide graphs and tables using the test data.

Richard Wade (rik@rikwade.com)

