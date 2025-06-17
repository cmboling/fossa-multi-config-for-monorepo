#!/usr/bin/env python
# coding: utf-8

from setuptools import setup, find_packages


def main():
    setup(
        name='desktop_ipc_interfaces',
        version='0.0.1',
        author='Box',
        author_email='desktop-team@box.com',
        zip_safe=False,
        packages=find_packages(),
        include_package_data=True,
        install_requires=['thrift'],
    )


if __name__ == '__main__':
    main()
