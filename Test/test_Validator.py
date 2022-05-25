import Validator


def test_validate_course_id_good():
    assert Validator.validate_couseID("123")


def test_validate_course_id_too_long():
    assert not Validator.validate_couseID("1234")


def test_validate_course_id_not_numbers():
    assert not Validator.validate_couseID("entotrefire")


def test_validate_course_good():
    assert Validator.validate_course("Systemudvikling")


def test_validate_course_too_short():
    assert not Validator.validate_course("Sund")


def test_validate_timefrome_is_too_long():
    assert not Validator.validate_timefrome("123456")


def test_validate_timefrome_is_not_numbers():
    assert not Validator.validate_timefrome("hello")


def test_validate_timefrom_not_contain_sign():
    assert not Validator.validate_timefrome("1000")


def test_validate_timefrom_is_good():
    assert Validator.validate_timefrome("10:00")


def test_validate_timeuntil_is_too_long():
    assert not Validator.validate_timeuntil("98765")


def test_validate_timeuntil_is_not_numbers():
    assert not Validator.validate_timeuntil("world")


def test_validate_timeuntil_not_cotain_sign():
    assert not Validator.validate_timeuntil("1300")


def test_validate_timeuntil_is_good():
    assert Validator.validate_timeuntil("13:00")


def test_validate_zoom_is_too_long():
    assert not Validator.validate_zoom("234")


def test_validate_zoom_is_not_number():
    assert not Validator.validate_zoom("four")


def test_validate_zoom_is_good():
    assert Validator.validate_zoom("0")
