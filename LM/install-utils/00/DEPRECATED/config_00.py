#!/usr/bin/env python3
# @file: config_00.py
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
from configparser import ConfigParser

## package_items = ((repository, package name)),...)


def read_config(config_filename = "config-00.ini"):
    """
    Makes a ConfigParser object from the configuration file.
    returns 'config'
    """
    config = ConfigParser(allow_no_value = True)
    config.read(config_filename)
    return config

def report_from_configfile(config_filename = "config-00.ini"):
    """
    Sends a pretty report from the 'config_filename'
    to the standard console stdout.
    """
    config = read_config(config_filename = config_filename)
    print("configuration file:", config_filename)
    line_fmt = "package {package} from repository {repository}"
    for section in config.sections():
        print(30 * "=")
        print("section ", section)
        package_items = config[section]
        for package, repository  in package_items.items():
            print(line_fmt.format(package=package,
                                  repository=repository))

def aptitude_update():
    """
    Calls aptitude and sends the output to stderr.
    """
    cmd = "aptitude -y update"
    output = subprocess.getoutput(cmd)
    print(output, file=sys.stderr)

def add_apt_repository(repository):
    """
    Calls add-apt-repository on repository if its value
    is not None.
    Sends the output to stderr.
    """
    cmd = "add-apt-repository -y {repository}".format(repository = repository)
    print(cmd, file=sys.stderr)
    output = subprocess.getoutput(cmd)
    aptitude_update()
    print(output, file=sys.stderr)

def aptitude_install_package(package):
    """
    Calls aptitude install on package.
    """
    cmd = "aptitude install -y {package}".format(package = package)
    output = subprocess.getoutput(cmd)
    print (output, file=sys.stderr)

def install_package_from_repository(package, repository):
    """
    Adds the repository if necessary and
    installs the package.
    """
    print(60*"=", file=sys.stderr)
    print("installing ", package, " from repository ",
          repository, file=sys.stderr)
    if repository is not None:
    	add_apt_repository(repository = repository)
    	aptitude_update()
    aptitude_install_package(package=package)

def install_packages_from_config_file(config_filename = "install-00.ini",
                                      section = "install-00"):
    """
    Calls read_config and installs the packages in 'section'."
    """
    config = read_config(config_filename = config_filename)
    section = config.get(section, None)
    if section is None:
       fmt = "configuration file {config_filename} has no section {section}"
       msg = fmt.format(config_filename = config_filename,
                        section = section)
       e = NoneTypeException(msg)
       raise e
    package_items = config[section].items()
    for  package, repository in package_items:
        install_package_from_repository(repository, package)


def _script():
    """
    Executed if this module is called
    as a script.
    """
    report_from_configfile(config_filename = "install-00.ini")
##    aptitude_update()
##    install_packages_from_config_file(config_filename = "install-00.ini",
##                                      section = "install-00")

if __name__ == "__main__":
    _script()
    pass
