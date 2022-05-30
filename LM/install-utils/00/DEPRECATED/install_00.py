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
      (None, "python3-pip"),
      (None, "idle"),
    # (None, "micro"),
    # (None, "jove"),
    # ("ppa:kelleyk/emacs", "emacs27"),
    ##  (None, "git"),
    # (None, "hypnotix"),
      (None, "gnome-system-tools"),
    # (None, "dissenter"),
      (None, "build-essential"),
    ##  (None, "python3-virtualenv"),
    # (None, "pandoc"),
    ##  (None, "fuse"),
    ##  (None, "python3-venv"),
    ##  (None, "ffmpeg"),
    # (None, "mg"),
      (None, "most"),
    # (None, "direnv"),
    ##  (None, "terminator"),
    # (None, "screen"),
    ## (None, "libva"),
    # (None, "hub"),
    # ("ppa:mkusb/ppa", "mkusb"),
    #  (None, "sublime-text"),
    ##   (None, "retext"),
    ########### emacs28 dependencies ######
    ##### https://justyn.io/til/compile-emacs-27-on-centos-7/
    #   (None, "GConf2-devel"),
    #   (None, "Xaw3d-devel"),
    #   (None, "dbus-devel"),
    #   (None, "dbus-glib-devel"),
    #   (None, "dbus-python"),
    #   (None, "gcc"),
    #   (None, "giflib-devel"),
    #   (None, "gnutls-devel"),
    #   (None, "gpm-devel"),
    #   (None, "gtk+-devel"),
    #   (None, "gtk2-devel"),
    #   (None, "ImageMagick"),
    #   (None, "ImageMagick-devel"),
    #   (None, "jansson-devel"),
    #   (None, "libX11-devel"),
    #   (None, "libXft-devel"),
    #   (None, "libXpm-devel"),
    #   (None, "libjpeg-devel"),
    #   (None, "libpng-devel"),
    #   (None, "libtiff-devel"),
    #   (None, "libungif-devel"),
    #   (None, "make"),
    #   (None, "ncurses-devel"),
    #   (None, "pkgconfig"),
    #   (None, "texi2html"),
    #   (None, "texinfo"),
    #   (None, "libncurses-devel"),
    #   (None, "libtinfo-devel"), 
    #   (None, "libncurses-devel"),
    #   (None, "libterminfo-devel"), 
    #   (None, "libcurses-devel"), 
    #   (None, "libtermcap-devel"),

    )

def add_apt_repository(repository):
    """
    Calls add-apt-repository on repository if its value
    is not None.
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

def install_package_from_repository(repository, package):
    """
    Adds the repository if necessary and
    installs the package.
    """
    print(60*"=", file=sys.stderr)
    print("installing ", package, " from repository ", repository, file=sys.stderr)
    if repository is not None:
    	add_apt_repository(repository)
    	aptitude_update()
    aptitude_install_package(package)

def install_packages(package_items = package_items):
    """
    items is ((repository,package), ...)
    """
    for repository, package in package_items:
        install_package_from_repository(repository,package)

def aptitude_update():
    """
    """
    cmd = "aptitude -y update"
    output = subprocess.getoutput(cmd)
    print(output, file=sys.stderr)

def _script():
    """
    Executed if this module is called
    as a script.
    """
    aptitude_update()
    install_packages(package_items = package_items)

if __name__ == "__main__":
    _script()

