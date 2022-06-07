## Installation

1. Add the repository URL via the Hassio Add-on Store Tab: **https://github.com/TenySmart/HassioAddon**
2. Configure the "ModbusTCP2MQTT" add-on.
3. Start the "ModbusTCP2MQTT" add-on.

## Configuration

**Note**: _Remember to restart the add-on when the configuration is changed._

```yaml
Inverter_host: Your Inverter Hostname/IP
Inverter_port: Your Inverter Port (Default: 502). If you have a WiNet-S dongle set to 8082
Scan_interval: 10->600
Scan_timeout: 3->60
log_level: INFO|WARNING|ERROR|DEBUG
Connection: "Sungrow"
Smart_meter: Set to true if you are using meter
Scan_level: BASIC|STANDARD|DETAIL|ALL
```


### Option `Scan_level` 
 - `BASIC`: Solar Generation
 - `STANDARD`: This is the most useful data for day to day
 - `DETAIL`: This should be everything your inverter supports
 - `ALL`: This will try every register, you will get lots of 0/65535 responses for registers not supported. 

  
### Option: `Scan_interval` 
Increase scan_interval in case you get "Modbus connection failed" at run time.

### Option: `Log_level`
- `error`: Show error only
- `debug`: Shows detailed debug information.
- `info`: Default informations.
- `warning`: Little alerts.

### MQTT Broker:
Your MQTT Broker address and credentials. If you don't know what this is, install this addon:
https://github.com/home-assistant/hassio-addons/tree/master/mosquitto

