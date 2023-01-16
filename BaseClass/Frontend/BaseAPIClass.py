from pathlib import Path

import requests


class BaseFacadeClass():


    tempData = {}
    def pretty_print_POST(self, request):
        """
        At this point it is completely built and ready
        to be fired; it is "prepared".

        However pay attention at the formatting used in
        this function because it is programmed to be pretty
        printed and may differ from the actual request.
        """
        print('{}\n{}\r\n{}\r\n\r\n{}\n{}'.format(
            '-----------START-----------',
            request.method + ' ' + request.url,
            '\r\n'.join('{}: {}'.format(k, v) for k, v in request.headers.items()),
            request.body, '-----------END-----------',
            ))

