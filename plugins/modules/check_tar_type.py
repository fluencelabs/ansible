#!/usr/bin/python

from ansible.module_utils.basic import AnsibleModule
import platform


def check_tar_type(module):
    cmd = ['tar', '--version']
    rc, out, err = module.run_command(cmd, check_rc=False)

    if rc != 0 or ('GNU tar' not in out and 'bsdtar' not in out):
        return None, out
    if 'GNU tar' in out:
        return 'gnu', out
    else:
        return 'bsd', out


def main():
    module = AnsibleModule(
        argument_spec={}
    )

    tar_type, tar_output = check_tar_type(module)

    if tar_type == 'gnu':
        module.exit_json(
            changed=False,
            msg="GNU tar is installed.",
            tar_type=tar_type)
    else:
        fail_msg = "Non GNU tar is installed."
        if platform.system() == 'Darwin':
            fail_msg += " You can install GNU tar with 'brew install gnu-tar'."
        module.fail_json(msg=fail_msg, tar_output=tar_output)


if __name__ == '__main__':
    main()
