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

## Credits
Original work by Richard Wade (rik@rikwade.com).

