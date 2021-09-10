## Configuration

**Note**: _Remember to restart the add-on when the configuration is changed._


```yaml
inverter_ip: Your Inverter IP
inverter_port: Your Inverter Port (Default 502)
model: one of supported models
timeout: 3->60
scan_interval: 10-300
mqtt_host: 'core-mosquitto'
mqtt_port: '1883'
mqtt_username: BROKER_USER
mqtt_password: BROKER_PASS
log_level: INFO|WARNING|DEBUG
```

Your MQTT Broker address and credentials. If you don't know what this is, install this addon:
https://github.com/home-assistant/hassio-addons/tree/master/mosquitto

