FROM ubuntu:22.04

ARG DEBIAN_FRONTEND=noninteractive
ENV DOCKER "YES"
ENV LANG C.UTF-8

RUN set -xe \
    && apt-get update \
    && apt-get install --no-install-recommends -y \
      openssh-server sudo systemd \
      python3 python-is-python3 \
      curl \
    && apt-get autoclean -y \
    && apt-get autoremove -y

RUN set -xe \
    && groupadd ubuntu \
    && useradd -g ubuntu -G sudo -m -s /bin/bash ubuntu \
    && echo 'ubuntu:ubuntu' | chpasswd \
    && echo 'ubuntu ALL=(ALL) NOPASSWD: ALL' > /etc/sudoers.d/ubuntu \
    && chmod 0440 /etc/sudoers.d/ubuntu

RUN set -xe \
    && sed -i -e 's/#PasswordAuthentication.*/PasswordAuthentication yes/g' /etc/ssh/sshd_config \
    && sed -i -e 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config \
    && sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

RUN set -xe \
    && systemctl mask ssh.socket && systemctl mask sshd.socket \
    && systemctl disable sshd && systemctl enable ssh \
    && chown -R ubuntu:ubuntu /home/ubuntu

CMD ["/lib/systemd/systemd"]
