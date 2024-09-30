#!/usr/bin/python

from __future__ import absolute_import, division, print_function
__metaclass__ = type

import os
import hashlib
import json
import shutil
from datetime import datetime
from ansible.module_utils.basic import AnsibleModule


def calculate_file_hashes(directory):
    """Calculate the hashes of all files in the directory."""
    file_hashes = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hashes[filepath] = calculate_hash(filepath)
    return file_hashes


def calculate_hash(filepath):
    """Calculate the SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(filepath, 'rb') as f:
            while chunk := f.read(8192):
                sha256.update(chunk)
        return sha256.hexdigest()
    except IOError:
        return None


def load_previous_hashes(hash_file):
    """Load the previous hashes from the specified file."""
    if os.path.exists(hash_file):
        with open(hash_file, 'r') as f:
            return json.load(f)
    return {}


def save_current_hashes(hash_file, hashes):
    """Save the current hashes to the specified file."""
    with open(hash_file, 'w') as f:
        json.dump(hashes, f, indent=4)


def compare_hashes(previous_hashes, current_hashes):
    """Compare the current and previous hashes to determine if changes occurred."""
    changes_detected = False

    # Compare file additions and deletions
    previous_files = set(previous_hashes.keys())
    current_files = set(current_hashes.keys())

    added_files = current_files - previous_files
    deleted_files = previous_files - current_files
    changed_files = []

    # Compare file hash changes
    for file in current_files.intersection(previous_files):
        if current_hashes[file] != previous_hashes[file]:
            changed_files.append(file)

    # Determine if any changes occurred
    if added_files or deleted_files or changed_files:
        changes_detected = True

    return changes_detected, added_files, deleted_files, changed_files


def create_archive(directory, backup_directory):
    """Create an archive of the directory with a timestamp in the backup directory."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    archive_name = f"backup_{timestamp}.tar.gz"
    archive_path = os.path.join(backup_directory, archive_name)

    try:
        shutil.make_archive(
            archive_path.replace(
                '.tar.gz',
                ''),
            'gztar',
            directory)
        return archive_path, None
    except Exception as e:
        return None, str(e)


def main():
    # Define the arguments that the module will accept
    module_args = dict(
        directory=dict(type='str', required=True),
        hash_file=dict(type='str', required=True),
        backup_directory=dict(type='str', required=True)
    )

    # Initialize the module
    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True
    )

    directory = module.params['directory']
    hash_file = module.params['hash_file']
    backup_directory = module.params['backup_directory']

    # Calculate current hashes
    current_hashes = calculate_file_hashes(directory)

    # Load previous hashes
    previous_hashes = load_previous_hashes(hash_file)

    # Compare hashes
    changes_detected, added_files, deleted_files, changed_files = compare_hashes(
        previous_hashes, current_hashes)

    archive_path = None
    error_message = None

    if changes_detected:
        # Create archive if any changes detected
        archive_path, error_message = create_archive(
            directory, backup_directory)

        if error_message:
            module.fail_json(msg=f"Failed to create archive: {error_message}")

        # Save the current hashes for future runs
        save_current_hashes(hash_file, current_hashes)

    # Return the result
    module.exit_json(
        changed=changes_detected,
        added_files=list(added_files),
        deleted_files=list(deleted_files),
        changed_files=changed_files,
        archive_path=archive_path
    )


if __name__ == '__main__':
    main()
