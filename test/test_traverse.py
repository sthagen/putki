import putki.traverse as traverse


def test_is_path_ok():
    assert traverse.is_path('example/s/structures.yml')


def test_is_path_ok_too():
    assert traverse.is_path('')


def test_is_path_fail():
    assert not traverse.is_path(True)


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


def test_follow_example_s():
    code, message, root, claims = traverse.follow('example/s/structures.yml')
    assert code == 0
    assert message == ''
    assert root
    assert claims


def test_walk_fs_example_s_missing_components():
    traverse.ROI = 'c'
    assert traverse.walk_fs({}, 'example/s/') == 1
