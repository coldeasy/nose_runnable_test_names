Nose Runnable Test Names
========================

Using this plugins allows you to copy and paste the test description outputted by nose directly back to the runner.

```shell
$ nosetests --with-runnable-test-names -v2
my_module:MyTestCase.my_test_method ... ok
----------------------------------------------------------------------
Ran 1 tests in 0.001s

OK

$ nosetests my_module:MyTestCase.my_test_method
my_module:MyTestCase.my_test_method ... ok
----------------------------------------------------------------------
Ran 1 tests in 0.001s

OK
```

