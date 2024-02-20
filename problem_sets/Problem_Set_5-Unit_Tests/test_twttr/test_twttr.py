from twttr import shorten

def test_single():
    assert shorten("cat") == "ct"
    assert shorten("shorten") == "shrtn"

def test_multiple():
    assert shorten("testing multiple words") == "tstng mltpl wrds"

def test_numbers():
    assert shorten("229090") == "229090"

def test_capitals():
    assert shorten("USA") == "S"
    assert shorten("Amsterdam") == "mstrdm"

def test_punctuation():
    assert shorten("Hello, World!") == "Hll, Wrld!"
