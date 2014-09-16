import os
from nose.plugins import Plugin


class RunnableTestNames(Plugin):
    name = 'runnable-test-names'

    def options(self, parser, env=os.environ):
        super(RunnableTestNames, self).options(parser, env=env)

    def configure(self, options, conf):
        super(RunnableTestNames, self).configure(options, conf)

    def describeTest(self, nosetest):
        test_case = nosetest.test
        mod, cls_name = test_case.__module__, test_case.__class__.__name__
        return '%s:%s.%s' % (mod, cls_name, test_case._testMethodName)
