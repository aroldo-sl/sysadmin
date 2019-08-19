.. file:  README.txt

.. date:  2013-04-02

.. author: Aroldo Souza-Leite


lb-buildout
===========





The buildout configuration for LiveBase (mitcon GmbH) 

Operating System
----------------

Developed and tested on Linux.

It could work in MSWindows under the circumstances that the usage of the Windows
file system very Linux like is (no special characters in directory paths, etc). There may be other requirements for this buildout conifuguration work on Windows.


Miscellaneous remarks
---------------------

- Python virtual environment: it is still necessary to work in an isolated
  Python environemnt for this buildout.

- version conflicts: there may still be version conflicts with Pygments, 
  docutils and even with different versions of zc.buildout. Clean the
  Python virtual environment site-packages and the buildout egg cache from
  these eggs and try ./lb-clean-bootstrap-buldout.bat again.

- we are always using JW Kolman's `bootstrap.py` for Grok

- we are always using distribute (`python bootstrap.py -d`)

- in some cases we try to have eggs available offline


Tests
-----

TODO: activate `bin/py.test` and `bin\test`


 






