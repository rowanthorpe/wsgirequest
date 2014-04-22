def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    x=0
    while x < 10:
        yield 'Hello World ' + str(x) + '\r\n'
        x += 1
