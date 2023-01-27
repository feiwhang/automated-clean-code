import automated_clean_code.histlib


def test_create_counter_hist():
    lines = ["a", "b", "a", "c", "b"]
    expected = {"a": 2, "b": 2, "c": 1}
    assert automated_clean_code.histlib.create_counter_hist(lines) == expected


def test_find_min_counter():
    counter = {"a": 2, "b": 2, "c": 1}
    expected = ("c", 1)
    assert automated_clean_code.histlib.find_min_counter(counter) == expected


def test_find_max_counter():
    counter = {"a": 2, "b": 2, "c": 1}
    expected = ("a", 2)
    assert automated_clean_code.histlib.find_max_counter(counter) == expected
