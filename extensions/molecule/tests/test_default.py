import testinfra.utils.ansible_runner
import pytest
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.mark.parametrize("directory", [
    "/opt/nox/nox-1",
    "/opt/nox/nox-2",
])
def test_nox_directories(host, directory):
    d = host.file(directory)

    assert d.is_directory
    assert d.exists
    assert d.user == "nox"
    assert d.mode == 493

def test_nox_cleanup(host):
    directory = host.file("/opt/nox/nox-0")
    service = host.service("nox-@0")

    assert not service.is_running
    assert not service.is_enabled
    assert not directory.exists


def test_ipfs_download(host):
    f = host.file("/usr/local/bin/ipfs")

    assert f.is_file
    assert f.exists


@pytest.mark.parametrize("service", [
    "nox-@1",
    "nox-@2",
])
def test_nox_is_running(host, service):
    service = host.service(service)

    assert service.is_running
    assert service.is_enabled


def test_user_created(host):
    assert host.user("nox").exists
    assert "nox" in host.user("nox").groups
