ARG BUILD_FROM
FROM $BUILD_FROM
ENV LANG C.UTF-8

#WORKDIR /
COPY . /
# Install requirements for add-on
#RUN apk add --no-cache python3-dev py3-pip g++

RUN pip3 install -r /tmp/requirements.txt

CMD ["python3", "solariot.py"]

LABEL io.hass.version="VERSION" io.hass.type="addon" io.hass.arch="armhf|aarch64|i386|amd64"
