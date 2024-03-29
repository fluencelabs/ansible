# fluencelabs.provider.nox

Install and configure [Nox](https://github.com/fluencelabs/nox/) - Rust
implementation of the Fluence network peer.

## Usage

See this [example](https://github.com/fluencelabs/ansible/blob/main/example/)

### Cleanup nox state

Rerun playbook with `nox_cleanup_state` set to `true`:
```bash
ansible-playbook nox.yml -e "nox_cleanup_state=true"
```

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

See [defaults/](https://github.com/fluencelabs/ansible/blob/main/roles/nox/defaults) for details and examples.

#### `fluence_project_dir`

- directory that contains provider settings, configs and secrets generated by
  [Fluence CLI](https://github.com/fluencelabs/cli) from `provider.yaml` config.
  Shared in collection.
- type: string

Should be put to `files/` directory where you run this role.

#### `fluence_instance_id`

- instance id to assing to target. Shared in collection.
- type: string

#### `nox_version`

- version of nox
- type: string

#### `nox_dir`

- root nox directory
- type: string
- default:
    ```yml
    nox_dir: "/opt/fluence/nox"
    ```

It will contain everything this role creates: nox binaries, configs, secrets.

#### `nox_unit_file`

- systemd unit file
- type: string
- default: see [defaults/main.yml](https://github.com/fluencelabs/blob/main/roles/nox/defaults/main.yml)

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

- whether to cleanup nox state
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
