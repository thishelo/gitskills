from wsgiref.simple_server import make_server


class Application(object):


    def __init__(self, environ, start_response):

        self.start_response = start_response

        self.path = environ['PATH_INFO']


    def __iter__(self):

        if self.path == '/':

            status = '200 OK'

            response_headers = [('Content-type', 'text/html')]

            self.start_response(status, esponse_headers)

            yield 'Hello,World!'.encode('utf-8')


        elif self.path == '/wsgi':

            status = '200 OK'

            response_headers = [('Content-type', 'text/html')]

            self.start_response(status, response_headers)

            yield 'Hello,WSGI!'.encode('utf-8')


        else:

            status = '404 NOT FOUND'

            response_headers = [('Content-type', 'text/html')]

            self.start_response(status, response_headers)

            yield '404 NOT FOUND'.encode('utf-8')


if __name__ == "__main__":

    app = make_server('127.0.0.1', 8000, Application)

    print('Serving HTTP on port 8000...')

    app.serve_forever()