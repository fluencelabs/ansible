#!/usr/bin/python

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import subprocess
import shutil
from ansible.module_utils.basic import AnsibleModule


def check_kvm_ok():
    """Check if the kvm-ok binary exists and run it to check virtualization."""
    # Check if 'kvm-ok' exists
    if shutil.which('kvm-ok') is None:
        return False, "The 'kvm-ok' binary is not found. Virtualization support cannot be checked."

    try:
        # Run the 'kvm-ok' command
        result = subprocess.run(
            ['kvm-ok'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        if result.returncode == 0:
            return True, result.stdout.decode('utf-8').strip()
        else:
            return False, "Virtualization is disabled. Nox will not be able to run VMs."
    except Exception as e:
        return False, f"Failed to execute 'kvm-ok': {str(e)}"


def main():
    # Define the arguments that the module will accept (no arguments in this
    # case)
    module_args = dict()

    # Initialize the Ansible module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    # Check if kvm-ok is available and run it
    success, message = check_kvm_ok()

    # If kvm-ok is missing or virtualization is disabled, warn the user
    if not success:
        module.warn(message)

    # Return success (even if there are warnings) and the appropriate message
    module.exit_json(changed=False, msg="Virtualization check completed.")


if __name__ == '__main__':
    main()
