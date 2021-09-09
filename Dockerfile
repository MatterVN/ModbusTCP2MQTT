#ARG BUILD_FROM=hassioaddons/base-python
ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

#WORKDIR /
COPY . /
RUN chmod a+x /run.sh



# Install requirements for add-on
RUN apk add --no-cache python3-dev py3-pip g++
RUN pip install -U pymodbus paho-mqtt dweepy influxdb SungrowModbusTcpClient readsettings

#CMD [ "/run.sh" ]
CMD ["python3", "solariot.py", "-v"]


#ENV PYTHONPATH="/config:$PYTHONPATH"



#LABEL io.hass.version="VERSION" io.hass.type="addon" io.hass.arch="armhf|aarch64|i386|amd64"
