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

import getopt
import sys
import yaml
##Load options
options = {'inverter':{},'exports':[{}]}
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
    sensor = [{},{},{},{},{},{},{},{},{}]

    sensor[0]['name'] = "Daily Generation"
    sensor[0]['sensor_type'] = "sensor"
    sensor[0]['register'] = "daily_power_yields"
    sensor[0]['dev_class'] = "energy"
    sensor[0]['state_class'] = "total_increasing"
    
    sensor[1]['name'] = "Active Power"
    sensor[1]['sensor_type'] = "sensor"
    sensor[1]['register'] = "total_active_power"
    sensor[1]['dev_class'] = "power"
    sensor[1]['state_class'] = "measurement"
    
    sensor[2]['name'] = "Load Power"
    sensor[2]['sensor_type'] = "sensor"
    sensor[2]['register'] = "load_power"
    sensor[2]['dev_class'] = "power"
    sensor[2]['state_class'] = "measurement"
    
    sensor[3]['name'] = "Meter Power"
    sensor[3]['sensor_type'] = "sensor"
    sensor[3]['register'] = "meter_power"
    sensor[3]['dev_class'] = "power"
    sensor[3]['state_class'] = "measurement"

    sensor[4]['name'] =  "Export to Grid"
    sensor[4]['sensor_type'] = "sensor"
    sensor[4]['register'] = "export_to_grid"
    sensor[4]['dev_class'] = "power"
    sensor[4]['state_class'] = "measurement"

    sensor[5]['name'] =  "Import from Grid"
    sensor[5]['sensor_type'] = "sensor"
    sensor[5]['register'] = "import_from_grid"
    sensor[5]['dev_class'] = "power"
    sensor[5]['state_class'] = "measurement"

    sensor[6]['name'] = "Temperature"
    sensor[6]['sensor_type'] = "sensor"
    sensor[6]['register'] = "internal_temperature"
    sensor[6]['dev_class'] = "temperature"
    sensor[6]['state_class'] = "measurement"

    sensor[7]['name'] = "Power State"
    sensor[7]['sensor_type'] = "binary_sensor"
    sensor[7]['register'] = "run_state"
    sensor[7]['dev_class'] = "running"
    sensor[7]['payload_on'] = "ON"
    sensor[7]['payload_off'] = "OFF"
    
    sensor[8]['name'] = "Phase A Voltage"
    sensor[8]['sensor_type'] = "sensor"
    sensor[8]['register'] = "phase_a_voltage"
    sensor[8]['dev_class'] = "voltage"
    sensor[8]['state_class'] = "measurement"
   
    options['exports'][0]['ha_sensors']= sensor

    
    with open('config.sg', 'w') as yaml_file:
      yaml.dump(options, yaml_file, default_flow_style=False)