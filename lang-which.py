from wsgiservice import Resource, get_app, mount, validate
from guess_language import guess_language


@mount('/')
class LangWhich(Resource):
    @validate('text')
    def POST(self, text):
        """
        Return the guessed language of POSTed text.

        Args:
            text (str): text to guess the language of.
        Returns:
            A dict with the guessed language.
            For example:

            {'language': 'en'}

        """
        lang = guess_language(text)
        return {'language': lang}


app = get_app(globals())

if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    port = 8080
    print 'Listening on port {p}'.format(p=port)
    make_server('', port, app).serve_forever()
