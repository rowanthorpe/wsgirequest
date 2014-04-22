def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    x=9
    while x >= 0:
        yield 'Hello World ' + str(x) + '\n'
        x -= 1
