import testinfra.utils.ansible_runner
import pytest
import os

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
        os.environ["MOLECULE_INVENTORY_FILE"]).get_hosts("all")


@pytest.mark.parametrize("directory", [
    "/opt/fluence/nox",
    "/opt/fluence/ccp",
    "/opt/fluence/promtail",
])
def test_directories(host, directory):
    d = host.file(directory)

    assert d.is_directory
    assert d.exists
    assert d.mode == 493


@pytest.mark.parametrize("config", [
    "/opt/fluence/nox/Config.toml",
    "/opt/fluence/ccp/Config.toml",
    "/opt/fluence/promtail/config.yml",
])
def test_config(host, config):
    d = host.file(config)

    assert d.is_file
    assert d.exists
    assert d.mode == 416


def test_ipfs_download(host):
    f = host.file("/usr/bin/ipfs")

    assert f.is_file
    assert f.exists


@pytest.mark.parametrize("service", [
    "nox",
    "ccp",
    "fluence-promtail",
])
def test_service_is_running(host, service):
    service = host.service(service)

    assert service.is_running
    assert service.is_enabled


@pytest.mark.parametrize("user", [
    "nox",
    "ccp",
])
def test_user_created(host, user):
    assert host.user(user).exists
    assert user in host.user(user).groups


@pytest.mark.parametrize("package", [
    "libhwloc-dev",
    "curl",
])
def test_packages_installed(host, package):
    assert host.package(package).is_installed
