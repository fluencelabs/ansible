FROM ubuntu:22.04

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get -y install \
        bridge-utils \
        dmidecode \
        dnsmasq \
        ebtables \
        iproute2 \
        iptables \
        libvirt-daemon-system \
        tini \
        sudo \
        ca-certificates \
        && \
    apt-get clean

RUN sed -i '/^#stdio_handler/ a\stdio_handler = "file"' /etc/libvirt/qemu.conf

CMD ["/usr/bin/tini", "/usr/sbin/libvirtd"]
