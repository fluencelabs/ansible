# Fluence promtail

Install, configure and maintain
[promtail](https://grafana.com/docs/loki/latest/clients/promtail/).

Promtail instance by default will collect only Nox and CCP logs. But you can
change config to anything you want.

You need to get `fluence_basicauth_username` and `fluence_basicauth_password`
from Cloudless Labs in order to use this role.

## Role Variables

See
[defaults/](https://github.com/fluencelabs/ansible/blob/main/roles/promtail/defaults/main.yml)
for details and examples.

#### `fluence_promtail_api_url`

- URL of Loki to feed logs to
- type: string
- default: "https://loki.fluence.dev/loki/api/v1/push"

#### `fluence_basicauth_username`

- basic auth username you get from Cloudless Labs to auth to Mimir.
- type: string

#### `fluence_basicauth_password`

- basic auth password you get from Cloudless Labs to auth to Mimir.
- type: string

#### `fluence_promtail_config`

- main
  [configuration](https://grafana.com/docs/loki/latest/clients/promtail/configuration/)
  file. Predefined and managed by Fluence Labs.
- default: please see
  [defaults/main.yml](https://github.com/fluencelabs/ansible/blob/main/roles/promtail/defaults/main.yml)
- type: map

#### `fluence_promtail_version`

- version to use
- type: string

#### `fluence_network`

- where it runs (kras or dar)
- type: string

#### `fluence_instance_id`

- instance id used as `instance` label in logs
- type: string

#### `fluence_promtail_user`

- owner of promtail process and files
- default: `promtail`
- type: string

#### `fluence_promtail_group`

- group of `fluence_promtail_user`
- default: `promtail`
- type: string

#### `fluence_promtail_download_url`

- url to get promtail archive from
- default: `https://releases.hashicorp.com`
- type: string

#### `fluence_promtail_unit`

- systemd unit file
- default: see
  [defaults/main.yml](https://github.com/fluencelabs/ansible/blob/main/roles/promtail/defaults/main.yml)
- type: string

#### `skip_handlers`

- skip restart/reload - useful when building images with Packer
- default: `false`

## Role Tags

- `cleanup` - stop and cleanup state

## Author

- **Anatolios Laskaris** - [nahsi](https://github.com/nahsi)
