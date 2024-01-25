# Nox

Install and configure [Nox](https://github.com/fluencelabs/nox/) - Rust
implementation of the Fluence network peer.

## Usage

### Generate provider config and nox configs

- Install
  [Fluence CLI](https://github.com/fluencelabs/cli?tab=readme-ov-file#installation-and-usage)
- Generate sample provider config in directory with ansible playbook:
    ```bash
    mkdir files/playground -p && cd files/playground
    fluence provider gen --env local --noxes 3 --no-input
    ```

- Adapt provider config in `playground/provider.yml` for your setup.
  For example:
    ```yaml
    # yaml-language-server: $schema=../.fluence/schemas/provider.json

    # Defines config used for provider set up

    # Documentation: https://github.com/fluencelabs/cli/tree/main/docs/configs/provider.md

    version: 0

    env: local

    computePeers:
      nox-0:
        computeUnits: 1
      nox-1:
        computeUnits: 1
      nox-2:
        computeUnits: 1

    offers:
      offer:
        maxCollateralPerWorker: 1
        minPricePerWorkerEpoch: 0.1
        computePeers:
          - nox-0
          - nox-1
          - nox-2

    nox:
      # you can write config overrides with yaml syntax using camelCase
      systemServices:
        enabled:
            - aqua-apfs
            - decider
            - trust-graph

      # or you can write config in toml
      # some options can be set only with rawConfig
      # this has highest priority when merging
      rawConfig: |
        allowed_binaries = [
          "/usr/bin/curl",
          # we need to set path to ipfs binary that was downloaded by role
          "{{ nox_dir }}/ipfs",
        ]

        [system_services]
            [aqua-apfs]
              external_api_multiaddres = "/ip4/ipfs.playground.com/tcp/5001"
              local_api_multiaddres = "/ip4/ipfs.service.consul/tcp/5001"
            decider:
              worker_ipfs_multiaddr = "/dns4/ipfs.playground.com/tcp/5001"
              network_api_endpoint = "https://somechain.com"
    ```

- Have a look at secrets config at `.fluence/provider-secrets.yaml` - it should be made private and not commited to git

- Regenerate nox configs
    ```bash
    fluence provider gen
    ```

### Install and configure nox using ansible role

- Populate ansible inventory with required variables
  - Create `inventory/group_vars/all/nox.yml` with common for all nox instances
    variables:
    ```yml
    nox_version: "0.16.13"
    nox_ipfs_version: "0.25.0"
    nox_project_dir: "playground"
    ```
  - Assign nox instances to hosts, for example by using `host_vars`:
    - `inventory/host_vars/instance-0/nox.yml`
      ```yml
      nox_instances: [0, 1]
      ```
    - `inventory/host_vars/instance-1/nox.yml`
      ```yml
      nox_instances: [2]
      ```

- Download role and prepare playbook:
  - Create `requirements.yml`
      ```yml
      roles:
        - name: fluencelabs.nox
          version: 0.1.0
          name: nox
      ```
  - Install nox role
      ```bash
      ansible-galaxy install -r requirements.yml --force
      ```
  - Create `nox.yml` playbook:
      ```yml
      - hosts: "all"
        become: true
        roles:
          - "nox"
      ```
- Install nox
    ```bash
    ansible-playbook nox.yml
    ```

This will run `nox-0` and `nox-1` on `instance-0` and `nox-2` on `instance-1`.

### Cleanup nox state

Rerun playbook with `nox_cleanup_state` set to `true`:
```bash
ansible-playbook nox.yml -e "nox_cleanup_state=true"
```

### Reassign instances to different host

`nox-0` and `nox-1` runs on `instance-0` and `nox-2` on `instance-1`.

- `inventory/host_vars/instance-0/nox.yml`
  ```yml
  nox_instances: [0, 1]
  ```
- `inventory/host_vars/instance-1/nox.yml`
  ```yml
  nox_instances: [2]
  ```

Reassign `nox-0` to `instance-1`

- `inventory/host_vars/instance-0/nox.yml`
  ```yml
  nox_instances: [1]
  ```
- `inventory/host_vars/instance-1/nox.yml`
  ```yml
  nox_instances: [2, 0]
  ```

and run playbook:
```bash
ansible-playbook nox.yml
```

This will stop `nox-0` at `instance-0` and will run it on `instance-1`.

### Install nox snapshot from PR

Only for Fluence Labs members.

- Go to GitHub to e2e run from your PR, for example
  https://github.com/fluencelabs/nox/actions/runs/7409293504 - `7409293504` is
  run id
- Rerun role providing your `GITHUB_TOKEN` as env variable:
    ```bash
    GITHUB_TOKEN=<your_token> ansible-playbook nox.yml -e "nox_run_id=7409293504"
    ```

## Role Variables

See [defaults/](https://github.com/fluencelabs/deployment/blob/main/ansible/defaults) for details and examples.

#### `nox_version`

- version of nox
- type: string

#### `nox_instances`

- list of nox instances to install on target
- type: list

#### `nox_dir`

- root nox directory
- type: string
- default:
    ```yml
    nox_dir: "/opt/nox"
    ```

It will contain everything this role creates: IPFS binary, nox instances
subdirectories (`nox-1`, `nox-foo` etc) with nox binaries, configs and state.

#### `nox_project_dir`

- directory that contains configs and secrets generated by
  [Fluence CLI](https://github.com/fluencelabs/cli) from `provider.yaml` config.
- type: string
- default:
    ```yml
    nox_project_dir: ".fluence"
    ```

Should be put to `files/` directory where you run this role.

#### `nox_unit_file`

- systemd unit file
- type: string
- default: see [defaults/main.yml](https://github.com/fluencelabs/deployment/blob/main/ansible/defaults/main.yml)

#### `nox_user`

- owner of Nox process and files
- type: string
- default:
    ```yml
    nox_user: "nox"
    ```

#### `nox_group`

- group of `nox_user`
- type: string
- default:
    ```yml
    nox_group: "nox"
    ```

#### `nox_cleanup_state`

- whether to cleanup nox state.
- type: bool
- default:
    ```yml
    nox_cleanup_state: false
    ```

#### `nox_run_id`

- GitHub actions run id of workflow in
  [nox e2e run](https://github.com/fluencelabs/nox/actions/workflows/e2e.yml).
  Used by Fluence Labs internally to install a snapshot version of nox for
  testing. `GITHUB_TOKEN` is required.
- type: string

## Author

- **Anatolios Laskaris** - [nahsi](https://github.com/nahsi)
