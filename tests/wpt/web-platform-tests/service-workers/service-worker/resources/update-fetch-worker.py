import time

def main(request, response):
    # no-cache itself to ensure the user agent finds a new version for each update.
    headers = [('Cache-Control', 'no-cache, must-revalidate'),
               ('Pragma', 'no-cache')]

    content_type = ''
    extra_body = ''

    content_type = 'application/javascript'
    headers.append(('Content-Type', content_type))

    extra_body = "self.onfetch = (event) => { event.respondWith(fetch(event.request)); };"

    # Return a different script for each access.  Use .time() and .clock() for
    # best time resolution across different platforms.
    return headers, '/* %s %s */ %s' % (time.time(), time.clock(), extra_body)

