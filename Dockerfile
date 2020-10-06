FROM alpine:edge

# Add project source
WORKDIR /usr/src/musicbot
COPY . ./

# Install dependencies
RUN apk update \
&& apk add --no-cache \
  ca-certificates \
  ffmpeg \
  opus \
  python3 \
  py3-pip \
  py3-wheel \
  libsodium-dev \
\
# Install build dependencies
&& apk add --no-cache --virtual .build-deps \
  gcc \
  git \
  libffi-dev \
  make \
  musl-dev \
  python3-dev \
\
# Install pip dependencies
&& pip3 install --no-cache-dir -r requirements.txt \
\
# Clean up build dependencies
&& apk del .build-deps

# Create auto playlist
COPY ./config/_autoplaylist.txt ./config/autoplaylist.txt

ENV APP_ENV=docker

ENTRYPOINT ["python3", "dockerentry.py"]
