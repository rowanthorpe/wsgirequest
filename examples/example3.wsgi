import time

def application(environ, start_response):
    content = """<html>\r\n<head>\r\n<title>An Example Page</title>\r\n</head>\r\n<body>\r\nHello World, this is a very simple HTML document.\r\n</body>\r\n</html>\r\n"""
    req_time = time.strftime("%a, %d %b %Y %H:%M:%S %Z")
    content_len = len(content)
    start_response('200 OK', [
        ('Content-Type', 'text/html; charset=UTF-8'),
        ('Date', req_time),
        ('Server', 'wsgirequest/0.1'),
        ('Content-Length', content_len),
        ('Connection', 'close'),
        ('Cache-Control', 'no-cache')])
    yield content
