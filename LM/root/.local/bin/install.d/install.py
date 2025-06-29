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
    subprocess.run(cmd)
    _slog.debug(f"installed {package_name}")

def test_install_package():
    """
    Tests 'install_package'.
    """
    install_package()

def _script():
    """
    Runs if this module is called as a script.
    """
    test_install_package()

if __name__ == "__main__":
    _script()


