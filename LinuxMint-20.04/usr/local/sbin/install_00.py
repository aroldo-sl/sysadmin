#!/usr/bin/env python3
# @file: install_00.py
# @author: Aroldo Souza-Leite
# @date: 2021-05-05
# @modified: 2021-05-05
# @comment: Python script
"""
Adds package repositories and installs Debian
packages.
"""
# imports
import sys
import subprocess
from pprint import pprint, pformat

## package_items = ((repository, package name)),...)
package_items = (
    # (None, "micro"),
    # ("ppa:kelleyk/emacs", "emacs27"),
    # (None, "git"),
    # (None, "hypnotix"),
    # (None, "gnome-system-tools"),
    # (None, "dissenter"),
    # (None, "build-essential"),
    # (None, "python3-virtualenv"),
    # (None, "pandoc"),
    # (None, "fuse"),
    # (None, "python3-venv"),
    # (None, "ffmpeg"),
    # (None, "mg"),
    # (None, "most"),
    # (None, "direnv"),
    (None, "terminator"),
    )

def add_apt_repository(repository):
    """

    Calls add-apt-repository on repository if its value
    is not None.
    """
    if repository is None:
        print ("no reposiory")
        return
    cmd = "add-apt-repository -y {repository}".format(repository = repository)
    print(cmd)
    output = subprocess.getoutput(cmd)
    aptitude_update()
    print(output)

def aptitude_install_package(package):
    """
    Calls aptitude install on package.
    """
    cmd = "aptitude install -y {package}".format(package = package)
    print(cmd)
    output = subprocess.getoutput(cmd)
    print (output)

def install_package_from_repository(repository, package):
    """
    Adds the repository if necessary and
    installs the package.
    """
    add_apt_repository(repository)
    aptitude_install_package(package)
    print()

def install_packages(package_items = package_items):
    """
    items is ((repository,package), ...)
    """
    pprint(package_items)
    for repository, package in package_items:
        install_package_from_repository(repository,package)

def aptitude_update():
    """
    """
    cmd = "aptitude -y update"
    output = subprocess.getoutput(cmd)
    print(output)

def _script():
    """
    Executed if this module is called
    as a script.
    """
    aptitude_update()
    install_packages(package_items = package_items)

if __name__ == "__main__":
    _script()

