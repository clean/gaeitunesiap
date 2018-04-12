# -*- coding: utf-8 -*-
from google.appengine.api import urlfetch
import json


PRODUCTION_VALIDATION_URL = "https://buy.itunes.apple.com/verifyReceipt"
SANDBOX_VALIDATION_URL = "https://sandbox.itunes.apple.com/verifyReceipt"
STATUS_SANDBOX_RECEIPT_ERROR = 21007


_ERROR_CODES = {
    21000: 'The App Store could not read the JSON object you provided.',
    21002: 'The data in the receipt-data property was malformed or missing.',
    21003: 'The receipt could not be authenticated.',
    21004: 'The shared secret you provided does not match the shared secret on file for your account.',
    21005: 'The receipt server is not currently available.',
    21006: 'This receipt is valid but the subscription has expired. When this status code is returned to your server, the receipt data is also decoded and returned as part of the response.',
    21007: 'This receipt is from the test environment, but it was sent to the production environment for verification. Send it to the test environment instead.',
    21008: 'This receipt is from the production environment, but it was sent to the test environment for verification. Send it to the production environment instead.',
    21010: 'This receipt could not be authorized. Treat this the same as if a purchase was never made.'
}


class Error(Exception):
    pass


def verify(receipt_data, password=None, exclude_old_transactions=True,
        sandbox=False):

    payload = {
            'receipt-data': receipt_data,
            'password': password,
            'exclude-old-transactions': exclude_old_transactions
            }

    res = urlfetch.fetch(
        url=SANDBOX_VALIDATION_URL if sandbox else PRODUCTION_VALIDATION_URL,
        method=urlfetch.POST,
        payload=json.dumps(payload),
        validate_certificate=True
        )
    data = json.loads(res.content)
    if data['status'] in _ERROR_CODES:
        raise Error(_ERROR_CODES[data['status']])
    return data['receipt']

