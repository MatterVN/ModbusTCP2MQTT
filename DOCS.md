## Installation

1. Add the repository URL via the Hassio Add-on Store Tab: **https://github.com/MatterVN/HassioAddon**
2. Configure the "ModbusTCP2MQTT" add-on.
3. Start the "ModbusTCP2MQTT" add-on.

## Configuration

**Note**: _Remember to restart the add-on whenever the configuration is changed._

```yaml
Inverter_host: Your Inverter Hostname/IP
Inverter_port: Your Inverter Port (Default: 502). If you have a WiNet-S dongle set to 8082
Inverter_model: Force the add on to use your specific model. Leave blank for auto detection.
Smart_meter: Set to true if you are using meter
Connection: Sungrow|Modbus|HTTP
Scan_level: BASIC|STANDARD|DETAIL|ALL
Scan_interval: 10->600
Scan_timeout: 3->60
log_level: INFO|WARNING|ERROR|DEBUG
```
### Option `Connection` 
 - `Sungrow`: default connection method
 - `HTTP`: try this option if you are using Wifi-S dongle

### Option `Scan_level` 
 - `BASIC`: State, Solar Generation, Active Power
 - `STANDARD`: Power, Voltage, Meter (mostly use)
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
The add on requires `Home Assistant Mosquitto Broker` Add-on. To install this addon, have a look at:
https://github.com/home-assistant/hassio-addons/tree/master/mosquitto

