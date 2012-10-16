"""
VersionedSet unit tests.
"""
import doctest
import sys

from django.test import TestCase


class DoctestTestCase(TestCase):
    def test_run_doctest(self):
        class DummyStream:
            content = ''

            def write(self, text):
                self.content += text

        dummy_stream = DummyStream()
        before = sys.stdout
        sys.stdout = dummy_stream

        doctest.testfile('doctests.txt')
        sys.stdout = before

        content = dummy_stream.content
        if content:
            print >>sys.stderr, content
            self.fail()
