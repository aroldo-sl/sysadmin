#!/usr/bin/env python3
"""
Installs packages from 'packages.toml'.
"""
import os
from tomllib import load
from pprint import pformat
import subprocess
from pathlib import Path

# # #  [logging]
def _make_slog():
    """
    Diese Funktion benutzt nur die Standardbibliothek.

    Da diese Funktion nur einen ad hoc Logger erstellt,
    importier sie innerhalb der Funktion, sehr untypischerweise.
    Normalerweise sollten die imports modulweit gelten.
    """
    import sys   # non-module-global import: bad Python style!
    import time
    import logging
    logging.basicConfig(
        format = ("\n%(levelname)s:[%(name)s][%(asctime)s]"
                  "[%(module)s.%(funcName)s]\n%(message)1s"),
        stream = sys.stderr)
    _slog = logging.getLogger(__name__ + str(time.time()).replace('.','_'))
    _slog.setLevel(logging.DEBUG)
    return _slog

_slog = _make_slog() # _slog ist Modulweit sichtbar.



def retrieve_data(toml_filename = 'packages.toml'):
    """
    Retrieves the data from the TOML file.
    """
    with open(toml_filename, "rb") as toml_file:
        data = load(toml_file)
    _slog.debug("TOML data.")
    return data

def display_data(toml_filename = 'packages.toml'):
    """
    Displays the TOML data.
    """
    data = retrieve_data(toml_filename)
    pretty_data = pformat(data)
    return pretty_data
    

def install_package(package_name = "git"):
    """
    Installs one deb package.
    """
    cmd = ["apt", "install", "-y", package_name]
    _slog.debug(f"installing {package_name}")
    subprocess.run(cmd)

def test_install_package():
    """
    Tests 'install_package'.
    """
    install_package()

def add_repository_list(repository_list =
        ("deb http://gb.archive.ubuntu.com/ubuntu jammy main",)):
    """
    Adds new apt repositories from the repository_list.
    """
    # because I need 'add-apt-repository'
    install_package(package_name = "software-properties-common")
    subprocess.run(["apt","update", "-y"])
    for repository_name in repository_list:
        _slog.debug(f"Adding repository '{repository_name}'.")
        subprocess.run(["add-apt-repository",
                        repository_name, "-y"])

def test_add_repository_list():
    """
    Tests 'add_repository_list'.
    """
    add_repository_list()
                   
def install_section_packages(toml_filename = "packages.toml",
                             section_header = "general"):
    """
    Reads the entries from one section and install them
    if the 'value' is '', that is, if no new package
    repository has to be added.
    """
    data = retrieve_data(toml_filename)
    section = data[section_header]
    repository_list = [repository_name \
                       for repository_name in section.values()
                       if not repository_name == ""]
    add_repository_list(repository_list = repository_list)
    package_names = section.keys()
    _slog.debug(f"installing section '{section_header}'")
    for package_name in package_names:
        install_package(package_name = package_name)
    
def test_install_section_packages():
    """
    Tests install_section_packages.
    """
    install_section_packages(section_header = "Emacs")

def _script():
    """
    Runs if this module is called as a script.
    """
    # test_install_package()
    # test_add_repository_list()
    # test_install_section_packages()
    __filepath__ = Path(__file__)
    workdir_path = __filepath__.parent
    os.chdir(workdir_path)
    workdir_path = Path.cwd()
    _slog.info(f"work directory:{workdir_path}")
    toml_filename ="packages.toml"
    assert Path(toml_filename).resolve() in workdir_path.iterdir(), '"packages.toml" not found'
    section_headers = [
        #"general",
        "Emacs",
        #"Python",
        #"desktop",
        ]
    for section_header in section_headers:
        install_section_packages(toml_filename = toml_filename,
                                 section_header = section_header)
        
if __name__ == "__main__":
    _script()


