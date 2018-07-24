
import pytest
from phonebook import Phonebook

@pytest.fixture
def phonebook(request):
    phonebook = Phonebook()
    def cleanup_phonebook():
        phonebook.clear()
    request.addfinalizer(cleanup_phonebook)
    return phonebook

def test_add_and_lookupentry(phonebook):
    #pytest.skip("WIP")
    phonebook.add("Bob", 123)
    assert 123 == phonebook.lookup("Bob") ,"not found"


def test_phonebook_names_and_number(phonebook):
    phonebook.add("Alice",12345)
    phonebook.add("Bob",54321)
    phonebook.add("Catty",87654)
    assert "Alice" in phonebook.names()
    assert 54321 in phonebook.numbers()

def test_values_in_phonebook(phonebook):
    phonebook.add("Alice", 12345)
    phonebook.add("Bob", 54321)
    phonebook.add("Catty", 87654)
    assert set(phonebook.names()) == {"Alice","Bob","Catty"}

def test_missing_entry_raises_keyerror(phonebook):
    with pytest.raises(KeyError):
        phonebook.lookup("Bob")
