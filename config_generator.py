#!/usr/bin/env python3
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#Test: config_generator.py --host=HOST --port=502 --model=model --mqtt_host=MQTT_HOST --mqtt_port=1883 --mqtt_user=MQTT_USER --mqtt_pass=MQTT_PASS --scan=10 --timeout=3 --connection=sungrow --meter=false --level=STANDARD --log_level=INFO


import getopt
import sys
import yaml
##Load options
options = {'inverter':{},'exports':[{}]}
sensors =[]
full_cmd_arguments = sys.argv
argument_list = full_cmd_arguments[1:]
short_options = 'h:p:o:t:s:c:m:l:L:M:P:U:A'
long_options = ['host=','port=','model=','timeout=','scan=','connection=','meter=','level=','log_level=',
                'mqtt_host=', 'mqtt_port=','mqtt_user=', 'mqtt_pass=']

def level(l):
    switcher={
            'BASIC': 0,
            'STANDARD': 1,
            'DETAIL': 2,
            'ALL': 3
        }
    return switcher.get(l, 1)

try:
    arguments, values = getopt.getopt(
        argument_list, short_options, long_options)
except getopt.error as e:
    raise ValueError('Invalid parameters!')
        

for current_argument, current_value in arguments:
    if current_value == 'null' or len(current_value) == 0 or current_value.isspace():
        pass
    elif current_argument in ("-h", "--host"):
        options['inverter']['host'] = current_value
    elif current_argument in ("-p", "--port"):
        options['inverter']['port'] = int(current_value)
    elif current_argument in ("-o", "--model"):
        options['inverter']['model'] = current_value
    elif current_argument in ("-t", "--timeout"):
        options['inverter']['timeout'] = int(current_value)
    elif current_argument in ("-s", "--scan"):
        options['inverter']['scan_interval'] = int(current_value)
    elif current_argument in ("-c", "--connection"):
        options['inverter']['connection'] = current_value.lower()
    elif current_argument in ("-m", "--meter"):
        options['inverter']['smart_meter'] = (current_value).lower() in ("yes","true","1")
    elif current_argument in ("-l", "--level"):
        options['inverter']['level'] = level(current_value)
    elif current_argument in ("-L", "--log_level"):
        options['inverter']['log_console'] = current_value.upper()
    elif current_argument in ("-M", "--mqtt_host"):
        options['exports'][0]['host'] = current_value 
    elif current_argument in ("-P", "--mqtt_port"):
        options['exports'][0]['port'] = int(current_value)
    elif current_argument in ("-U", "--mqtt_user"):
        options['exports'][0]['username'] = current_value 
    elif current_argument in ("-A", "--mqtt_pass"):
        options['exports'][0]['password'] = current_value 

options['exports'][0]['name'] = "mqtt" 
options['exports'][0]['enabled'] = True
options['exports'][0]['homeassistant']= True
    
#Basic Level sensor
sensors.append({'name': "Power State", 'sensor_type': "binary_sensor",
'register': "run_state",'dev_class': "running",
'payload_on': "ON",'payload_off': "OFF"})

sensors.append({'name': "Daily Generation", 'sensor_type': "sensor",
'register': "daily_power_yields", 'dev_class': "energy",
'state_class': "total_increasing"})

sensors.append({'name': "Active Power", 'sensor_type': "sensor",
'register': "total_active_power", 'dev_class': "power",
'state_class': "measurement"})



#Standard Level
if int(options['inverter']['level']) >= 1:
    sensors.append({'name': "Total DC Power", 'sensor_type': "sensor",
    'register': "total_dc_power", 'dev_class': "power",
    'state_class': "measurement"})
    
    sensors.append({'name': "Load Power Hybrid", 'sensor_type': "sensor",
    'register': "load_power_hybrid", 'dev_class': "power",
    'state_class': "measurement"})
    
    sensors.append({'name': "Export Power Hybrid", 'sensor_type': "sensor",
    'register': "export_power_hybrid", 'dev_class': "power",
    'state_class': "measurement"})
    
    sensors.append({'name': "Load Power", 'sensor_type': "sensor",
    'register': "load_power", 'dev_class': "power",
    'state_class': "measurement"})

    sensors.append({'name': "Phase A Voltage", 'sensor_type': "sensor",
    'register': "phase_a_voltage", 'dev_class': "voltage",
    'state_class': "measurement"})

    sensors.append({'name': "Phase B Voltage", 'sensor_type': "sensor",
    'register': "phase_b_voltage", 'dev_class': "voltage",
    'state_class': "measurement"})

    sensors.append({'name': "Phase C Voltage", 'sensor_type': "sensor",
    'register': "phase_c_voltage", 'dev_class': "voltage",
    'state_class': "measurement"})

    sensors.append({'name': "Phase A Current", 'sensor_type': "sensor",
    'register': "phase_a_current", 'dev_class': "current",
    'state_class': "measurement"})

    sensors.append({'name': "Phase B Current", 'sensor_type': "sensor",
    'register': "phase_b_current", 'dev_class': "current",
    'state_class': "measurement"})

    sensors.append({'name': "Phase C Current", 'sensor_type': "sensor",
    'register': "phase_c_current", 'dev_class': "current",
    'state_class': "measurement"})

    sensors.append({'name': "Battery Power", 'sensor_type': "sensor",
    'register': "battery_power", 'dev_class': "power",
    'state_class': "measurement"})

    sensors.append({'name': "Battery Power", 'sensor_type': "sensor",
    'register': "battery_power", 'dev_class': "power",
    'state_class': "measurement"})

    sensors.append({'name': "Battery SOC", 'sensor_type': "sensor",
    'register': "battery_level", 'dev_class': "percent",
    'state_class': "measurement"})

    sensors.append({'name': "Battery Health", 'sensor_type': "sensor",
    'register': "battery_state_of_healthy", 'dev_class': "percent",
    'state_class': "measurement"})

    if options['inverter']['smart_meter'] == True:
        sensors.append({'name': "Meter Power", 'sensor_type': "sensor",
        'register': "meter_power", 'dev_class': "power",
        'state_class': "measurement"})
        
        sensors.append({'name': "Meter A phase Power", 'sensor_type': "sensor",
        'register': "meter_a_phase_power", 'dev_class': "power",
        'state_class': "measurement"})
        
        sensors.append({'name': "Meter B phase Power", 'sensor_type': "sensor",
        'register': "meter_b_phase_power", 'dev_class': "power",
        'state_class': "measurement"})
        
        sensors.append({'name': "Meter C phase Power", 'sensor_type': "sensor",
        'register': "meter_c_phase_power", 'dev_class': "power",
        'state_class': "measurement"})
        
        sensors.append({'name': "Export Power", 'sensor_type': "sensor",
        'register': "export_power", 'dev_class': "power",
        'state_class': "measurement"})
        
        sensors.append({'name': "Power Meter", 'sensor_type': "sensor",
        'register': "power_meter", 'dev_class': "power",
        'state_class': "measurement"})
        
        sensors.append({'name': "Import from Grid", 'sensor_type': "sensor",
        'register': "import_from_grid", 'dev_class': "power",
        'state_class': "measurement"})

        sensors.append({'name': "Export to Grid", 'sensor_type': "sensor",
        'register': "export_to_grid", 'dev_class': "power",
        'state_class': "measurement"})

#Detail Level
if options['inverter']['level'] >= 2:
    sensors.append({'name': "Temperature", 'sensor_type': "sensor",
    'register': "internal_temperature", 'dev_class': "temperature",
    'state_class': "measurement"})
    
    sensors.append({'name': "Battery Temperature", 'sensor_type': "sensor",
    'register': "battery_temperature", 'dev_class': "temperature",
    'state_class': "measurement"})
    
    sensors.append({'name': "Total Active Power", 'sensor_type': "sensor",
    'register': "total_active_power", 'dev_class': "power",
    'state_class': "measurement"})
    
    sensors.append({'name': "Total Reactive Power", 'sensor_type': "sensor",
    'register': "total_reactive_power", 'dev_class': "power",
    'state_class': "measurement"})
  
options['exports'][0]['ha_sensors']= sensors

with open('config.sg', 'w') as yaml_file:
    yaml.dump(options, yaml_file, default_flow_style=False)
