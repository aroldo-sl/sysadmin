#!/usr/bin/env python3
# @file: install.py
# @author: Aroldo Souza-Leite
# @date: 2021-05-05
# @modified: 2021-05-05
# @comment: Python script for installing packages
# @comment: in Linux Mint
"""
Adds package repositories and installs Debian
packages.
"""
# imports
import sys
import subprocess
from pprint import pprint, pformat
from configparser import ConfigParser
## #
## ## the default ini file to be read from.
if len(sys.argv) < 2:
   _config_filename =  "install.ini"
else:
    _config_filename = sys.argv[1]
## ## the default line format for printing a report
_config_line_fmt = "entry {key} has value {value}"

def read_config_file(config_filename = _config_filename,
                     allow_no_value = True):
    """
    Makes a ConfigParser object that parses
    the configuration file.
    returns 'config_parser'
    """
    config_parser = ConfigParser(allow_no_value = allow_no_value)
    config_parser.read(config_filename)
    return config_parser

def report_config_section(config_parser,
                          section_title,
                          config_line_fmt = _config_line_fmt):
    """
    Writes a report from one section of a config parser
    """
    section = config_parser[section_title]
    config_items = section.items()
    for key, value in config_items:
          line = config_line_fmt.format(key = key, value = value)
          print (line)


def report_config_sections(config_filename = _config_filename,
                    config_line_fmt = _config_line_fmt):
    """
    Sends a pretty report from the 'config_filename'
    to the standard console stdout.
    """
    config_parser = read_config_file(config_filename = config_filename)
    print(60 * "=")
    print("configuration file:", config_filename)
    print(60 * "=")
    for section in config_parser.sections():
        print()
        print(section)
        print(60 * "-")
        report_config_section(config_parser = config_parser,
                              section_title = str(section),
                              config_line_fmt = config_line_fmt)
        print(60 * "-")                           
 
def aptitude_update():
    """
    Calls aptitude and sends the output to stdout.
    """
    cmd = "aptitude -y update"
    output = subprocess.getoutput(cmd)
    print(output, file=sys.stdout)

def add_apt_repository(repository):
    """
    Calls add-apt-repository on repository if its value
    is not None.
    Sends the output to stdout.
    """
    cmd = "add-apt-repository -y {repository}".format(repository = repository)
    print(cmd, file=sys.stdout)
    output = subprocess.getoutput(cmd)
    aptitude_update()
    print(output, file=sys.stdout)

def aptitude_install_package(package):
    """
    Calls aptitude install on package.
    """
    cmd = "aptitude install -y {package}".format(package = package)
    output = subprocess.getoutput(cmd)
    print (output, file=sys.stdout)

def install_package_from_repository(package, repository):
    """
    Adds the repository if necessary and
    installs the package.
    """
    print(60*"=", file=sys.stdout)
    print("installing ", package, " from repository ",
          repository, file=sys.stdout)
    if repository is not None:
    	add_apt_repository(repository = repository)
    	aptitude_update()
    aptitude_install_package(package=package)


def reinstall_certificates():
    """
    Reinstalls the certificates because of ppa.
    """
    cmd = "apt-get install --reinstall ca-certificates"
    output = subprocess.getoutput(cmd)
    print(output)

def install_packages_from_config_file(
                    config_filename = _config_filename,
                    section_titles = ()):
    """
    Calls read_config and installs the packages in 'section'."
    """
    line_fmt = "{section} -> {package} from repository {repository}"
    config_parser = read_config_file(config_filename = config_filename)
    for section in config_parser.sections():
        for package, repository in config_parser[section].items():
            line = line_fmt.format(
                   section = section,
                   package = package,
                   repository = repository)
            install_package_from_repository(package, repository)
 
def _script():
    """
    Executed if this module is called
    as a script.
    """
    report_config_sections()
    # reinstall_certificates()
    # install_packages_from_config_file()
##    aptitude_update()
##    install_packages_from_config_file(config_filename = "install-00.ini",
##                                      section = "install-00")

if __name__ == "__main__":
    _script()
    pass
