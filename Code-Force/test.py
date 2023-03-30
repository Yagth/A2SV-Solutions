def testCase(function, tests):
    
    testNumber = 0
    failedTests = 0

    for test in tests:
        result = function(**test['input']) == test['output']
        status = printStatus(result)
        if status == 'FAILED':
            failedTests += 1
        print("Test #",testNumber,status + "\n")
        testNumber += 1
    print("Summary of tests: ", (testNumber - failedTests), "/", testNumber, " Passed")
        

def printStatus(status):
    if status:
        return 'PASSED'
    else:
        return 'FAILED'