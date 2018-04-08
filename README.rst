gaeitunesiap
~~~~~~~~~~~~



Apple iTunes In-app purchase verification api for GAE environment

https://developer.apple.com/library/content/releasenotes/General/ValidateAppStoreReceipt/Chapters/ValidateRemotely.html


Quick example
-------------


.. sourcecode:: python

  import gaeitunesiap
  try:
    receipt = gaeitunesiap.verify(
        receipt_data=<The base64 encoded receipt data>,
        password=<Your app’s shared secret (a hexadecimal string)>,
        exclude_old_transactions=True,
        sandbox=True)
  except gaeitunesiap.Error as e:
    print 'Error occur: {}'.format(e)

Intalation
----------

.. sourcecode:: shell

  $ pip install git+https://github.com/romannowicki/gaeitunesiap.git#egg=gaeitunesiap
