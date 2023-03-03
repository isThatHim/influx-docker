# influx-docker
InfluxDB + Telgraf + Kapacitor + Chronograf

## Usage

### Running
```
$ docker-compose up
```

You will need to create the databases in InfluxDB in order to store time-series
values for the various metrics. The configuration currently uses two databases,
one for telemetry data and one for Synology SNMP data.

```
$ curl -i -XPOST http://localhost:8086/query --data-urlencode "q=CREATE DATABASE mdt"
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


## Credits
Original work by Richard Wade (rik@rikwade.com).

