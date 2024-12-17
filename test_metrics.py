from metrics import window_max, window_average, window_stddev
from test_run import assert_equal

from config import windowmax2_out, windowmax3_out, \
        windowmax4_out, windowmax7_out, empty, full, \
        windowavg2_out, windowavg3_out, windowavg4_out, \
        windowavg7_out, windowdev2_out, \
        windowdev3_out, windowdev4_out, windowdev7_out


if __name__ == "__main__":
    print("window_max function test")
    result = window_max([1, 2, 3, 4, 5, 6, 7], 1)
    assert_equal(result, full, "1")

    result = window_max([1, 2, 3, 4, 5, 6, 7], 2)
    assert_equal(result, windowmax2_out, "2")

    result = window_max([1, 2, 3, 4, 5, 6, 7], 3)
    assert_equal(result, windowmax3_out, "3")

    result = window_max([1, 2, 3, 4, 5, 6, 7], 4)
    assert_equal(result, windowmax4_out, "4")

    result = window_max([1, 2, 3, 4, 5, 6, 7], 7)
    assert_equal(result, windowmax7_out, "5")

    result = window_max([], 1)
    assert_equal(result, empty, "6")

    result = window_max([], 2)
    assert_equal(result, empty, "7")

    print("window_average function test")
    result = window_average([1, 2, 3, 4, 5, 6, 7], 1)
    assert_equal(result, full, "1")

    result = window_average([1, 2, 3, 4, 5, 6, 7], 2)
    assert_equal(result, windowavg2_out, "2")

    result = window_average([1, 2, 3, 4, 5, 6, 7], 3)
    assert_equal(result, windowavg3_out, "3")

    result = window_average([1, 2, 3, 4, 5, 6, 7], 4)
    assert_equal(result, windowavg4_out, "4")

    result = window_average([1, 2, 3, 4, 5, 6, 7], 7)
    assert_equal(result, windowavg7_out, "5")

    result = window_average([], 1)
    assert_equal(result, empty, "6")

    result = window_average([], 2)
    assert_equal(result, empty, "7")

    print("window_stddev function test")
    result = window_stddev([1, 2, 3, 4, 5, 6, 7], 1)
    assert_equal(result, empty, "1")

    result = window_stddev([1, 2, 3, 4, 5, 6, 7], 2)
    assert_equal(result, windowdev2_out, "2")

    result = window_stddev([1, 2, 3, 4, 5, 6, 7], 3)
    assert_equal(result, windowdev3_out, "3")

    result = window_stddev([1, 2, 3, 4, 5, 6, 7], 4)
    assert_equal(result, windowdev4_out, "4")

    result = window_stddev([1, 2, 3, 4, 5, 6, 7], 7)
    assert_equal(result, windowdev7_out, "5")

    result = window_stddev([], 1)
    assert_equal(result, empty, "6")

    result = window_stddev([], 2)
    assert_equal(result, empty, "7")
