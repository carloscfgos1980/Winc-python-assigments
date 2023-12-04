import main


def test_get_none():
    assert main.get_none() == None


# print(main.flatten_dict({'a': [42, 350], 'b': 3.14}))
# print(main.flatten_dict(({'a': 42, 'b': 3.14})))
# print(main.flatten_dict({'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}))
# print(main.flatten_dict({'a': [{'inner_inner_a': 42}]}))


def test_flatten_dict():
    assert main.flatten_dict({'a': 42, 'b': 3.14}) == [42, 3.14]
    assert main.flatten_dict({'a': [42, 350], 'b': 3.14}) == [[42, 350], 3.14]
    assert main.flatten_dict(
        {'a': {'inner_a': 42, 'inner_b': 350}, 'b': 3.14}) == [42, 350, 3.14]
    assert main.flatten_dict({'a': [{'inner_inner_a': 42}]}) == [42]
