# Changelog

## [0.3.5](https://github.com/fluencelabs/ansible/compare/v0.3.4...v0.3.5) (2024-09-05)


### Features

* trigger release ([#43](https://github.com/fluencelabs/ansible/issues/43)) ([f12bf3f](https://github.com/fluencelabs/ansible/commit/f12bf3f498fb835ff821843c3e37f032c96d6174))

## [0.3.4](https://github.com/fluencelabs/ansible/compare/v0.3.3...v0.3.4) (2024-08-30)


### Features

* nox vm support ([#40](https://github.com/fluencelabs/ansible/issues/40)) ([57782a7](https://github.com/fluencelabs/ansible/commit/57782a796a21e884f90dfca6a27e3d7a3fa23ebf))

## [0.3.3](https://github.com/fluencelabs/ansible/compare/v0.3.2...v0.3.3) (2024-07-30)


### Bug Fixes

* Temporary remove vm-sandboxing ([#36](https://github.com/fluencelabs/ansible/issues/36)) ([6fd9b35](https://github.com/fluencelabs/ansible/commit/6fd9b3592489dd1a6a4e0a36e40d4002371eba4c))

## [0.3.2](https://github.com/fluencelabs/ansible/compare/v0.3.1...v0.3.2) (2024-07-30)


### Bug Fixes

* Fix vmsandboxing role name ([#34](https://github.com/fluencelabs/ansible/issues/34)) ([2044a11](https://github.com/fluencelabs/ansible/commit/2044a11d9ed61dbea11b9324a997075fef6e49de))

## [0.3.1](https://github.com/fluencelabs/ansible/compare/v0.3.0...v0.3.1) (2024-07-24)


### Bug Fixes

* Use S3 to download nox and ccp snapshots ([#32](https://github.com/fluencelabs/ansible/issues/32)) ([d513e20](https://github.com/fluencelabs/ansible/commit/d513e20b8723147f3beb59ad634e652d5fb8dc5c))

## [0.3.0](https://github.com/fluencelabs/ansible/compare/v0.2.3...v0.3.0) (2024-07-19)


### ⚠ BREAKING CHANGES

* new VM sandboxing bootstrap role ([#28](https://github.com/fluencelabs/ansible/issues/28))

### Features

* new VM sandboxing bootstrap role ([#28](https://github.com/fluencelabs/ansible/issues/28)) ([501769d](https://github.com/fluencelabs/ansible/commit/501769d1a928d6b07c009498c65084d43bb7ff6a))

## [0.2.3](https://github.com/fluencelabs/ansible/compare/v0.2.2...v0.2.3) (2024-07-02)


### Bug Fixes

* Use s3 to download ccp artifact ([#25](https://github.com/fluencelabs/ansible/issues/25)) ([ae829d4](https://github.com/fluencelabs/ansible/commit/ae829d4a9332478d36d133b3fd0be91ded6f92af))

## [0.2.2](https://github.com/fluencelabs/ansible/compare/v0.2.1...v0.2.2) (2024-05-30)


### Features

* Add ability to run promtail for log collection ([#20](https://github.com/fluencelabs/ansible/issues/20)) ([a9d0429](https://github.com/fluencelabs/ansible/commit/a9d0429ea27cae66354057f953cb5df6c79a9365))
* Add prometheus role ([#23](https://github.com/fluencelabs/ansible/issues/23)) ([7da9c72](https://github.com/fluencelabs/ansible/commit/7da9c7247d15ab7c2bdcedfc4cf03f63aabc0dd5))

## [0.2.1](https://github.com/fluencelabs/ansible/compare/v0.2.0...v0.2.1) (2024-03-09)


### Bug Fixes

* Download ipfs to /usr/bin/ ([#16](https://github.com/fluencelabs/ansible/issues/16)) ([4f61a1b](https://github.com/fluencelabs/ansible/commit/4f61a1b096e90e7a62dbeaf609fcd114853e9522))

## [0.2.0](https://github.com/fluencelabs/ansible/compare/v0.1.3...v0.2.0) (2024-03-07)


### ⚠ BREAKING CHANGES

* Add ccp role and rewrite nox role to allow only one nox per host ([#9](https://github.com/fluencelabs/ansible/issues/9))

### Features

* Add ccp role and rewrite nox role to allow only one nox per host ([#9](https://github.com/fluencelabs/ansible/issues/9)) ([ac4bb6d](https://github.com/fluencelabs/ansible/commit/ac4bb6d6a477ee24dde70f88b20ec887dd87a735))

## [0.1.3](https://github.com/fluencelabs/ansible/compare/v0.1.2...v0.1.3) (2024-02-09)


### Bug Fixes

* Check if tar is GNU type ([#8](https://github.com/fluencelabs/ansible/issues/8)) ([780b466](https://github.com/fluencelabs/ansible/commit/780b4667ff05ccb0d6a841f11e5486a465edf2d5))
* Copy ipfs to `nox_dir` + various small fixes/cleanups ([#6](https://github.com/fluencelabs/ansible/issues/6)) ([171526c](https://github.com/fluencelabs/ansible/commit/171526c01a810aa8217d6ed7e68ac017e3142a86))

## [0.1.2](https://github.com/fluencelabs/ansible/compare/v0.1.1...v0.1.2) (2024-02-05)


### Bug Fixes

* Search for configs in `files/&lt;project&gt;/.fluence` ([#4](https://github.com/fluencelabs/ansible/issues/4)) ([216db21](https://github.com/fluencelabs/ansible/commit/216db2107c313453ab0dd3e34e2ffc1c16a72d56))

## [0.1.1](https://github.com/fluencelabs/ansible/compare/v0.1.0...v0.1.1) (2024-01-25)


### Features

* Add collection ([#1](https://github.com/fluencelabs/ansible/issues/1)) ([343b40e](https://github.com/fluencelabs/ansible/commit/343b40ee1e10d0b036387193bcef0b5ecd92815b))
