from flask import Flask, request, render_template, redirect
from shortener import return_url


application = Flask(__name__)


def bad_request(message):
    """Takes a supplied message and attaches it to a HttpResponse with code 400.
    Parameters:
    message - string containing the error message.
    Return values:
    An object with a message string and a status_code set to 400.
    """
    response = {'message': message}
    response.status_code = 400
    return response

@application.route('/<alias>', methods=['GET'])
def get_shortened(alias):
    """GET endpoint that takes an alias (shortened url) and redirects if successfull.
    Otherwise returns a bad request.
    Arguments:
    alias, the string representing a shortened url.
    Return values:
    A Flask redirect, with code 302.
    """

    url = return_url(alias)
    if type(url) is not str:
        return bad_request('Unknown alias.')
    else:
        return redirect(url, code=302)

if __name__ == '__main__':
    application.run(debug=True)