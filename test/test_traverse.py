import putki.traverse as traverse


def test_is_yaml_ok():
    assert traverse.is_yaml('example/s/structures.yml')


def test_is_yaml_ok_too():
    assert traverse.is_yaml('example/s/structures.yaml')


def test_is_yaml_fail():
    assert not traverse.is_yaml('example/s/structures.json')


def test_load_yaml_ok():
    assert traverse.load_yaml('example/s/structures.yml')


def test_load_yaml_fail():
    assert not traverse.load_yaml('example/s/not-present.yml')
