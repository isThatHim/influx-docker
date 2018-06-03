# influx-docker
A Skeleton InfluxDB + Kapacitor + Grafana

This repository contains a docker-compose file to bring up an integrated
Influxdata InfluxDB, Influxdata Kapacitor and Grafana. It is provided with a
Python script (data_source.py) which can be run to produce test data in the
database using metrics from the local machine.

## Usage

### Requirements
This system requires Docker, Python 3 and Python modules in the included
requirements.txt. To install the Python modules, use:
```
$ pip install -r requirements.txt
```

### Running
```
$ docker-compose up
```

will start the components. Given many people will be using this to work with
Model Driven Telemetry, the test script uses an InfluxDB database called 'mdt'.
In order to initialise this:

```
$ curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE mdt"
```

You may now execute the test script:
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

--
Richard Wade (rik@rikwade.com)
