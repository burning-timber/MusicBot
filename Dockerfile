FROM ubuntu:18.04

# Add project source
WORKDIR /usr/src/musicbot
COPY . ./

# Install dependencies
RUN apt-get update \
&& apt-get -y install \
  ca-certificates \
  ffmpeg \
  libopus0 \
  python3 \
  python3-pip \
  python3-wheel \
  libsodium-dev \
\
# Install build dependencies
&& apt-get -y install \
  libffi-dev \
  musl-dev \
  python3-dev \
\
# Install pip dependencies
&& pip3 install --no-cache-dir -r requirements.txt \
\
# Clean up build dependencies
&& apt-get clean

# Create auto playlist
COPY ./config/_autoplaylist.txt ./config/autoplaylist.txt

ENV APP_ENV=docker

ENTRYPOINT ["python3", "dockerentry.py"]
