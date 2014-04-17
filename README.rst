===========
wsgirequest
===========

Minimal commandline one-request WSGI server
-------------------------------------------

This has one argument - the path to the wsgi file. It accepts an HTTP request
on stdin, supplies the response (with headers) on stdout, and errors go to
stderr.

A large part of it is based on copy-pasting from the Python PEP-3333 page.

To see usage use the -h or --help option.

This is for troubleshooting and experimenting. Don't try and use it as a real
server. That would be silly.
