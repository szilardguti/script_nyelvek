from utils import duplaz, is_palindrome

def test_duplaz():
    assert duplaz(8) == 16
    assert duplaz(7) == 14
    assert duplaz(0) == 0
    assert duplaz(-1) == -2
    assert duplaz(-5) == -10
    

def test_is_palindrome():
    assert is_palindrome("gorog") == True
    assert is_palindrome("a") == True
    assert is_palindrome("hurka") == False
    assert is_palindrome("") == True
    assert is_palindrome("ab") == False
    assert is_palindrome("cc") == True
    assert is_palindrome("kek") == True
