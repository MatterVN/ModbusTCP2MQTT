#!/usr/bin/with-contenv bashio

HOST=$(bashio::config 'Inverter_host')
PORT=$(bashio::config 'Inverter_port')
MODEL=$(bashio::config 'Inverter_model')
SCAN_INTERVAL=$(bashio::config 'Scan_interval')
SCAN_TIMEOUT=$(bashio::config 'Scan_timeout')
CONNECTION=$(bashio::config 'Connection')
SMART_METER=$(bashio::config 'Smart_meter')
LEVEL=$(bashio::config 'Scan_level')
LOG_LEVEL=$(bashio::config 'Log_level')
MQTT_HOST=$(bashio::config 'Mqtt_host')
MQTT_PORT=$(bashio::config 'Mqtt_port')
MQTT_USER=$(bashio::config 'Mqtt_user')
MQTT_PASS=$(bashio::config 'Mqtt_pass')


if ! bashio::services.available "mqtt"; then
   bashio::exit.nok "No internal MQTT Broker found. Please install Mosquitto broker."
else
    MQTT_HOST=$(bashio::services mqtt "host")
    MQTT_PORT=$(bashio::services mqtt "port")
    MQTT_USER=$(bashio::services mqtt "username")
    MQTT_PASS=$(bashio::services mqtt "password")
    bashio::log.info "Configured'$MQTT_HOST' mqtt broker."
fi
python3 /config_generator.py --host=$HOST --port=$PORT --model=$MODEL --mqtt_host=$MQTT_HOST --mqtt_port=$MQTT_PORT --mqtt_user=$MQTT_USER --mqtt_pass=$MQTT_PASS --scan=$SCAN_INTERVAL --timeout=$SCAN_TIMEOUT --connection=$CONNECTION --meter=$SMART_METER --level=$LEVEL --log_level=$LOG_LEVEL
bashio::log.info "Generated config file."
exec python3 /sungather.py -c config.sg
