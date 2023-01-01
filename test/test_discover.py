import pathlib

import putki.discover as discover


def test_root_devault():
    assert discover.root() == str(pathlib.Path.cwd())


def test_root_cwd_is_root():
    assert discover.root('.') == str(pathlib.Path.cwd())


def test_root_within_not_existing():
    assert discover.root('non-existing-path') == ''


def test_root_within_is_without():
    assert discover.root('/') == ''
