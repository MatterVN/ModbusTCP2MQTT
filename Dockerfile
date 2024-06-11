ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

# Build arugments
ARG BUILD_VERSION
ARG BUILD_ARCH


COPY requirements.txt ./
RUN apk add --no-cache python3-dev py3-pip g++
RUN pip install --break-system-packages --upgrade pycryptodomex~=3.11.0 --no-cache-dir -r requirements.txt

COPY SunGather/ /
COPY SunGather/exports/ /exports
COPY run.sh /
COPY config_generator.py /

VOLUME /logs
VOLUME /config
# Install requirements for add-on
RUN chmod a+x /run.sh

CMD ["/run.sh"]

LABEL \ 
    io.hass.name="ModbusTCP2MQTT" \
    io.hass.description="Sungrow-SMA Solar inverter communication Addon" \
    io.hass.version=${BUILD_VERSION} \
    io.hass.type="addon" \
    io.hass.arch=${BUILD_ARCH}
