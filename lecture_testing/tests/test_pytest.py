import pytest

x = 4


@pytest.mark.skip(reason='Just skip')
def test_equals():
    assert x == 4


@pytest.mark.skipif(True, reason='x should be less than 5 to run test')
def test_skip_if():
    pass


@pytest.mark.smoke
def test_mark_smoke_1():
    print('smoke test 1')


@pytest.mark.smoke
def test_mark_smoke_2():
    print('smoke test 2')


@pytest.mark.guest
@pytest.mark.user
def test_double_marks_1():
    pass


@pytest.mark.user
def test_mark_user():
    pass


def test_clean_1():
    pass


def test_clean_2():
    pass
