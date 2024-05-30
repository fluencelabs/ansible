# Fluence prometheus

Install, configure and maintain
[prometheus](https://prometheus.io)

You need to get `fluence_basicauth_username` and `fluence_basicauth_password` from Cloudless Labs in order to use this role.

## Role Variables

See
[defaults/](https://github.com/fluencelabs/ansible/blob/main/roles/prometheus/defaults/main.yml)
for details and examples.

#### `fluence_prometheus_api_url`

- URL of Mimir to send metrics to
- type: string
- default: "https://mimir.fluence.dev/loki/api/v1/push"

#### `fluence_basicauth_username`

- basic auth username you get from Cloudless Labs to auth to Mimir.
- type: string

#### `fluence_basicauth_password`

- basic auth password you get from Cloudless Labs to auth to Mimir.
- type: string

#### `fluence_prometheus_config`

- main
  [configuration](https://prometheus.io/docs/prometheus/latest/configuration/configuration/)
  file. Predefined and managed by Cloudless Labs.
- default: please see
  [defaults/main.yml](https://github.com/fluencelabs/ansible/blob/main/roles/prometheus/defaults/main.yml)
- type: map

#### `fluence_prometheus_version`

- version to use
- type: string

#### `fluence_instance_id`

- instance id used as `instance` label in metrics
- type: string

#### `fluence_prometheus_user`

- owner of prometheus process and files
- default: `prometheus`
- type: string

#### `fluence_prometheus_group`

- group of `fluence_prometheus_user`
- default: `prometheus`
- type: string

#### `fluence_prometheus_download_url`

- url to get prometheus archive from
- default: `https://github.com/prometheus/prometheus/releases`
- type: string

#### `fluence_prometheus_unit`

- systemd unit file
- default: see
  [defaults/main.yml](https://github.com/fluencelabs/ansible/blob/main/roles/prometheus/defaults/main.yml)
- type: string

## Author

- **Anatolios Laskaris** - [nahsi](https://github.com/nahsi)
