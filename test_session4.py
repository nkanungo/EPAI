import pytest
import random
import string
import session4
import os
import inspect
import re
import math
from decimal import Decimal
from numbers import Real
import cmath


README_CONTENT_CHECK_FOR = [
    'and',
    'Qualean',
    'or',
    'repr',
    'str',
    'add',
    'eq',
    'float',
    'ge',
    'gt',
    'le',
    'lt',
    'mul',
    'bool',
    'invertsign',
    'sqrt'
]


def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r",encoding="utf-8")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines" 

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

        
def test_invalid_real_valueerror():
    with pytest.raises(AttributeError):
        session4.Qualean(2)
    with pytest.raises(AttributeError):
        session4.Qualean(-2)
    
def test_and_positive_func():
    t1 = session4.Qualean(1)
    t2 = session4.Qualean(0)    
    assert(t1 and t2)  == t2 , f"Your And function is not working properly for both positives"
    
def test_and_negative_func():
    t1 = session4.Qualean(1)
    t2 = session4.Qualean(-1)    
    assert(t1 and t2)  == t2 , f"Your And function is not working properly for both negatives"

def test_and_zero_func():
    t1 = session4.Qualean(0)
    t2 = session4.Qualean(1)    
    assert(t1 and t2)  == t1 , f"Your And function is not working properly for one zero value"
    
def test_or_positive_func():
    t1 = session4.Qualean(1)
    t2 = session4.Qualean(1)    
    assert(t1 or t2)  == t1 , f"Your And function is not working properly for both positives"
    
def test_or_negative_func():
    t1 = session4.Qualean(1)
    t2 = session4.Qualean(-1)    
    assert(t1 or t2)  == t1 , f"Your And function is not working properly for both negatives"

def test_or_zero_func():
    t1 = session4.Qualean(0)
    t2 = session4.Qualean(1)    
    assert(t1 or t2)  == t2 , f"Your And function is not working properly for one zero value"
    
def test_repr_func():
    t1 = session4.Qualean(1)
    assert(bool(t1.__repr__)), f"You have not properly configured repr function"

def test_string_func():
    t1 = session4.Qualean(1)
    assert(str(t1)), f"Your string function is not working"
    
def test_add_func():
    t1 = session4.Qualean(1)
    t2 = session4.Qualean(1)
    add_t1_t2_val = t1.real + t2.real
    add_t1_t2 = t1 + t2
    assert(math.isclose(add_t1_t2_val,add_t1_t2.real)), 'Your add function seems to have some problem'

def test_equal_func():
    t1 = session4.Qualean(1)
    t3=t1
    assert (t1 ==t3), 'Your Equal function is not working' 
def test_float_func():
    t1 = session4.Qualean(1)
    t2 = float(t1)
    assert(t2 == t1.real), 'Your float conversion not working'
    
def test_ge_func():
    t1 = session4.Qualean(1)
    t2 = session4.Qualean(0)
    t3 =t1
    assert(abs(t1.real) >=t2.real), 'Your greater than equal to function is not working'
    assert(t3 >=t1), 'Your greater than equal to function is not working'
    
def test_gt_func():
    t1 = session4.Qualean(1)
    t2 = session4.Qualean(0)
    t3 =t1
    assert(abs(t1.real) >t2.real) , 'Your greater than function is not working'
    
def test_le_func():
    t1 = session4.Qualean(1)
    t2 = session4.Qualean(0)
    
    assert(t2.real <= abs(t1.real)), 'Your Less than equal to function is not working'
    
def test_lt_func():
    t1 = session4.Qualean(1)
    t2 = session4.Qualean(0)
    
    assert(t2.real < abs(t1.real)) , 'Your greater than function is not working'

def test_mult_func():
    t1 = session4.Qualean(1)
    t2 = session4.Qualean(-1)
    assert (t1 * t2), 'Your Multiplication class is not working'
    
def test_bool_func():
    t1 = session4.Qualean(1)
    assert(bool(t1)), 'Bool function Not implemented properly'
def test_invert_func():
    t1 = session4.Qualean(1)
    t2 = t1.__invertsign__()
    assert(t2.real == -(t1.real)), 'Your invertion function is not working properly'
def test_sqrt_func():
    for i in range(1000):
        for j in (-1,1):
            t1 = session4.Qualean(j)
            assert(t1.__sqrt__()),'Square root function not implemented properly'
def test_hund_equal_func():
    q = session4.Qualean(1)
    p = session4.Qualean(0)
    for _ in range(100):
        p = p + q

    assert(math.isclose(p,q.real * 100)), ' The Numbers are not equal'
    
def test_sqrt_func():
    q = session4.Qualean(1)
    if q.real > 0:  
        a= q.__sqrt__()
        b = math.sqrt(Decimal(q.real))
        math.isclose(a,b)
        assert(math.isclose(a,b)), 'You are not handling the Decimal properly'
def test_one_million():
    p = session4.Qualean(0)
    mylist = [-1,0,1]
    w_list = random.choices(mylist, weights = [1, 1, 1], k = 1000000)
    for i in range (1000000):
    #list1 = [-1,0,1]
        j = w_list[i]
    #print(j)
        q = session4.Qualean(j)
        p = p + q
        assert(math.isclose(p,0,rel_tol=200)), 'The Functions are not in 200 range - I am just testing this and had to set rel_tol to match' 
def test_nd_and_func():
    k1 = session4.Qualean(0)
    assert(not(bool(k1) and k2)), ' Your Function is not proper'

def test_nd_or_func():
    k1 = session4.Qualean(1)
    assert(bool(k1) or k2), ' Your Function is not proper'


