#!/usr/bin/env python3
"""
Installs packages from 'packages.toml'.
"""
from tomllib import load
from pprint import pformat
import subprocess

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

def install_section_packages(toml_filename = "packages.toml",
                             section_header = "general"):
    """
    Reads the entries from one section and install them
    if the 'value' is '', that is, if no new package
    repository has to be added.
    """
    data = retrieve_data(toml_filename)
    section = data[section_header]
    package_names = [package_name for package_name in section \
                     if section[package_name] == '']
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
    test_install_section_packages()
    
if __name__ == "__main__":
    _script()


