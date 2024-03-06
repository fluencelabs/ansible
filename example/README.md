# Nox Setup with Ansible

This directory contains all necessary predefined files to setup Nox locally.

## Prerequisites

### Podman

Podman is an open-source, daemonless container engine that serves as a drop-in
replacement for Docker. Podman allows for easily starting containers with
`systemd`, which is required for Nox to run.

Download and install [Podman](https://podman.io/).

If on MacOS you can run:

```bash
brew install podman
```

### Fluence CLI

Install using commands from the
[FCLI readme](https://github.com/fluencelabs/cli?tab=readme-ov-file#using-install-script).

After installation, set a specific version of FCLI compatible with this guide:

```bash
fluence update --version 0.15.17
```

### MacOS

#### gnu-tar

Users of MacOS need to install `gnu-tar` for this collection of roles to work.

```bash
brew install gnu-tar
```

#### sshpass

Users of MacOS need to install (only for running examples) `sshpass`:

```bash
brew tap esolitos/ipa
brew install esolitos/ipa/sshpass
```

#### podman setup

Prepare podman with following commands:

```bash
podman machine init
podman machine start
```

## Setup Nox

- Clone this repo and change to `example` directory

```bash
git clone https://github.com/fluencelabs/ansible
cd example
```

- Create and activate python virtual environment

```bash
python3 -m venv ~/.virtualenvs/fluence/nox-ansible-demo
source ~/.virtualenvs/fluence/nox-ansible-demo/bin/activate
```

- Install python dependencies

```bash
pip3 install -r requirements.txt
```

- Install Ansible Provider collection

```bash
ansible-galaxy collection install fluencelabs.provider
```

- Start services and servers

```bash
podman-compose up -d --build
```

- Wait for all services to start and setup Noxes

```bash
ansible-playbook nox.yml -i inventory.yml
```

- When finished run cleanup

```bash
podman-compose down
```

## Do some things with Nox network

TODO:

- integrate IPC
- add provider registration
