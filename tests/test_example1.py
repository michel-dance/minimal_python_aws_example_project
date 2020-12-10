from merkle_example.example1 import example1
from merkle_example.example2 import example_tree


def test_that_we_can_execute_example_1_module_method():
    print(__file__)

    assert 0 == example1()


def test_that_we_can_create_merkle_hash():
    merkle_hash = example_tree("first string", "second message", "third message", "fourth message")

    merkle_hash_imposter = example_tree("hacked first string", "second message", "third message", "fourth message")

    assert merkle_hash != merkle_hash_imposter