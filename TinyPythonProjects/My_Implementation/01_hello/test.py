#!/usr/bin/env python
"""tests for hello.py"""

import os
from subprocess import getstatusoutput, getoutput

prog = './hello.py'


# Test 1 ----------
def test_exists():
    assert os.path.isfile(prog)

# Test 2 :
def test_runnable():
    """Runs using P3 """

    out = getoutput(f'python3 {prog}')
    print(out)
    assert out.strip() == 'Hello, World!'

# Test 3 :
def test_runnable_2():
    """Runs using P3 """

    out = getoutput(f'{prog}')
    print(out)
    assert out.strip() == 'Hello, World!'

#Test 4
def test_usage():

    for flag in ['-h','--help']:
        rv,out = getstatusoutput(f'{prog} {flag}')
        assert rv == 0
        assert out.lower().startswith("usage")

def test_implementation():
    for val in ['Universe']:
        for option in ['-n','--name']:
            rv, out = getstatusoutput(f'{prog} {option} {val}')
            assert rv == 0
            assert out.strip() == f'Hello, {val}!'

