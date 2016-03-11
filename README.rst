cmds for python
===============

A library that enables easy running and concatenation of bash commands in
python

Installation
------------

Install using pip::

    pip install cmds
    
Install using source code::

	git clone https://github.com/qiueer/cmds
	cd cmds
	python setup.py install


Usage
-----

Run commands as you would in bash::

    >>> from cmds import cmds
    >>> cmds('ls . | grep ".pyc"')
    cmds.pyc

Chain commands for the same effect::

    >>> cmds('ls . ').cmds('grep ".pyc"')
    cmds.pyc

Warning
-------

Please note that this library uses ``shell=True`` under the hood. This means
that this library is **NOT** suitable for running untrusted commands.
`(See explanation) <https://docs.python.org/2/library/subprocess.html#frequently-used-arguments>`_

Support + Contributing
----------------------

Feel free to make pull requests, or report issues via the repo:

https://github.com/qiueer/cmds
