# Nox Setup with Ansible

This directory contains all necessary predefined files to setup Nox locally.

You can follow this guide by [using predefined files](#Using-predefined-files)
or by [starting from scratch](#Starting-from-scratch).

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
fluence update --version 0.14.0
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

### Using Predefined Files

- Create and activate python virtual environment

```bash
python -m venv ~/.virtualenvs/fluence/nox-ansible-demo
source ~/.virtualenvs/fluence/nox-ansible-demo/bin/activate
```

- Install python dependencies

```bash
pip install -r requirements.txt
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

### Starting from Scratch

- Create project directories

```bash
# create project directory
mkdir ansible-demo && cd ansible-demo
# create necessary directories for ansible
mkdir -p files/demo
cd files/demo
```

- Initialize project

```bash
fluence provider init --no-input --env=local --noxes=3
```

- Update `provider.yaml` with nox config required for Ansible

```bash
cat <<EOF | patch provider.yaml
@@ -4,13 +4,14 @@
 
 # Documentation: https://github.com/fluencelabs/cli/tree/main/docs/configs/provider.md
 
-version: 0
-
 env: local
 
 computePeers:
   nox-0:
     computeUnits: 32
+    nox:
+      rawConfig: |
+        local = true
   nox-1:
     computeUnits: 32
   nox-2:
@@ -24,3 +25,39 @@
       - nox-0
       - nox-1
       - nox-2
+
+nox:
+  # you can write config overrides with yaml syntax using camelCase
+  systemServices:
+    enable:
+      - aqua-apfs
+      - decider
+
+  # or you can write config in toml
+  # some options can be set only with rawConfig
+  # this has highest priority when merging
+  rawConfig: |
+    allowed_binaries = [
+      "/usr/bin/curl",
+      # we need to set path to ipfs binary that was downloaded by role
+      "{{ nox_dir }}/ipfs",
+    ]
+
+    local = false
+    bootstrap_nodes = [
+      "/ip4/172.30.10.10/tcp/7771"
+    ]
+
+    [system_services.aqua_ipfs]
+    ipfs_binary_path = "{{ nox_dir }}/ipfs"
+    external_api_multiaddr = "/ip4/127.0.0.1/tcp/5001"
+    local_api_multiaddr = "/ip4/172.30.10.95/tcp/5001"
+
+    [system_services.decider]
+    decider_period_sec = 10
+    worker_ipfs_multiaddr = "/ip4/172.30.10.95/tcp/5001"
+    network_api_endpoint = "http://172.30.10.85:8545"
+    network_id = 31337
+    start_block = "earliest"
+    matcher_address = "0x0e1F3B362E22B2Dc82C9E35d6e62998C7E8e2349"
+    wallet_key = "0x3cc23e0227bd17ea5d6ea9d42b5eaa53ad41b1974de4755c79fe236d361a6fd5"
EOF
```

- Regenerate nox configs

```bash
fluence provider gen
```

- Change directory back

```bash
cd ../../
```

- Create and activate python virtual environment

```bash
python -m venv ~/.virtualenvs/fluence/nox-ansible-demo
source ~/.virtualenvs/fluence/nox-ansible-demo/bin/activate
```

- Install python dependencies

```bash
cat << EOF > requirements.txt
ansible==9.2.0
podman-compose
EOF
pip install -r requirements.txt
```

- Install Ansible Provider collection

```bash
ansible-galaxy collection install fluencelabs.provider
```

- Create ansible inventory file

```bash
cat << EOF > inventory.yml
all:
  children:
    servers:
      hosts:
        server-0:
          ansible_port: 2200
          nox_instances: [0]
        server-1:
          ansible_port: 2201
          nox_instances: [1,2]
      vars:
        ansible_user: "ubuntu"
        ansible_password: "ubuntu"
        ansible_host: "127.0.0.1"
        # fluencelabs.provider.nox variables
        nox_version: "0.18.0" # hardcoded compatible with fcli 0.18.1
        nox_project_dir: "demo"
        # fluencelabs.provider.ipfs_cli variables
        ipfs_cli_version: "0.26.0"
EOF
```

- Create playbook

```bash
cat <<EOF > nox.yml
- hosts: "all"
  become: true
  roles:
    - "fluencelabs.provider.nox"
EOF
```

- Copy `podmad-compose.yml`

```bash
cp ../podman-compose.yml .
```

- Start services and servers

```bash
podman-compose up -d --build
```

- Wait for all services to start and setup Noxes

```bash
ansible-playbook nox.yml -i inventory.yml
```

- When finished, run cleanup

```bash
podman-compose down
```

## Do some things with Nox network

TODO
