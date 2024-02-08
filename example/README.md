## Install Vagrant and VirtualBox

- [vagrant](https://developer.hashicorp.com/vagrant/install)
- [virtualbox](https://www.virtualbox.org/wiki/Downloads)

MacOS users with arm64 processors need to download
[beta build](https://www.virtualbox.org/wiki/Testbuilds) named
`macOS/ARM64 BETA`.

## Initialize Fluence project

- Use specific version of fcli compatible with this guide

```bash
fluence update --version 0.14.0
```

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
@@ -22,3 +22,33 @@
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
+    [system_services.aqua_ipfs]
+    external_api_multiaddr = "/ip4/127.0.0.1/tcp/5001"
+    local_api_multiaddr = "/ip4/192.168.56.100/tcp/5001"
+
+    [system_services.decider]
+    decider_period_sec = 10
+    worker_ipfs_multiaddr = "/ip4/192.168.56.100/tcp/5001"
+    network_api_endpoint = "http://192.168.56.100:8545"
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

## Prepare Ansible and setup Noxes

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
echo "ansible==9.2.0" > requirements.txt
pip install -r requirements.txt
```

- Install Ansible Provider collection

```bash
ansible-galaxy collection install fluencelabs.provider
```

- Create ansible inventory file

```bash
cat <<EOF > inventory.yml
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
cat <<EOF > playbook.yml
- hosts: "all"
  become: true
  roles:
    - "fluencelabs.provider.nox"
EOF
```

- Start servers vagrant

```bash
vagrant up
```

- Wait for all servers to start and setup Noxes

```bash
ansible-playbook playbook.yml -i inventory.yml
```

- When finished cleanup virtual machines

```bash
vagrant destroy
```
