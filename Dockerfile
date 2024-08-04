FROM nginx/unit:1.28.0-python3.10

COPY ./config/config.json /docker-entrypoint.d/config.json

RUN mkdir build

COPY . ./build

RUN apt update && apt install -y python3-pip                                  \
    && pip3 install -r /build/requirements.txt                               \
    && apt remove -y python3-pip                                              \
    && apt autoremove --purge -y                                              \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

EXPOSE 80
