from anagramma import (normalize, trivial_is_anagram, 
                        not_so_trivial_is_anagram)
                        
                        
def test_normalize():
    assert normalize("Clint Eastwood") == "clinteastwood"
    assert normalize("") == ""
    assert normalize("Testing Is Fun") == "testingisfun"
    assert normalize("oO0lI1\tuv") == "oo0li1uv"
    
    
def test_trivial_is_anagram():
    assert trivial_is_anagram("listen", "silent") == True
    assert trivial_is_anagram("A gentleman", "Elegant man") == True
    assert trivial_is_anagram("Clint Eastwood", "Old west action") == True
    assert trivial_is_anagram("", "not null") == False
    assert trivial_is_anagram("dormitory", "dirty room") == True
    assert trivial_is_anagram("WHAT", "THEAW") == False


def test_not_so_trivial_is_anagram():
    assert trivial_is_anagram("listen", "silent") == True
    assert trivial_is_anagram("A gentleman", "Elegant man") == True
    assert trivial_is_anagram("Clint Eastwood", "Old west action") == True
    assert trivial_is_anagram("", "not null") == False
    assert trivial_is_anagram("dormitory", "dirty room") == True
    assert trivial_is_anagram("WHAT", "THEAW") == False
