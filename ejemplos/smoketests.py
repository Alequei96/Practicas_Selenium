from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from assertions import AssertionTests
from searchtests import SearchTests


assertions_test = TestLoader().loadTestsFromTestCase(AssertionTests)
search_test = TestLoader().loadTestsFromTestCase(SearchTests)

smoke_test = TestSuite([assertions_test, search_test])

#Output creara otra carpeta llamada smoke-report
kwargs = {
    "output": 'smoke-report'
}

if __name__=='__main__':
    runner = HTMLTestRunner(**kwargs)
    runner.run(smoke_test)