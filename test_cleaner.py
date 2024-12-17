from cleaner import filter_nondigits, filter_outliers
from test_run import assert_equal

from config import clean1_out, clean2_out, clean3_out, \
    out1_out, out2_out, out3_out


if __name__ == "__main__":
    print("filter_nondigits function test")

    in_data = ["1\n", "2\n", "3\n", "4\n", "5\n", "6\n", "7\n"]
    assert_equal(filter_nondigits(in_data), clean1_out, "1")

    in_data = ["1\n", "\n", "3\n", "4\n", "5\n", "\n", "7\n"]
    assert_equal(filter_nondigits(in_data), clean2_out, "2")

    in_data = ["1\n", "None\n", "3\n", "4\n", "5\n", "None\n", "7\n"]
    assert_equal(filter_nondigits(in_data), clean2_out, "3")

    in_data = []
    assert_equal(filter_nondigits(in_data), clean3_out, "4")

    in_data = ["H", "e", "l", "l", "o"]
    assert_equal(filter_nondigits(in_data), clean3_out, "5")

    print("filter_outliers function test")

    in_data = [41, 42, 43, 44, 45, 46, 47]
    assert_equal(filter_outliers(in_data), out1_out, "1")

    in_data = [41, 342, 43, 44, 45, -46, 47]
    assert_equal(filter_outliers(in_data), out2_out, "2")

    in_data = [41, -42, 43, 44, 45, 346, 47]
    assert_equal(filter_outliers(in_data), out2_out, "3")

    in_data = [41, 342, 43, 44, 45, 346, 47]
    assert_equal(filter_outliers(in_data), out2_out, "4")

    in_data = [41, -42, 43, 44, 45, -46, 47]
    assert_equal(filter_outliers(in_data), out2_out, "5")

    in_data = []
    assert_equal(filter_outliers(in_data), out3_out, "6")

    in_data = [250, 250, 250, 250]
    assert_equal(filter_outliers(in_data), out3_out, "7")

    in_data = [30, 30, 30, 30]
    assert_equal(filter_outliers(in_data), out3_out, "8")
  

def filter_nondigits(data: list) -> list: 
    coconut=[]
    for digit in data:
        if digit.strip().isdigit():
            coconut.append(int(digit.strip()))
    return coconut



def filter_outliers(data:list,min_value=30, max_value=250)-> list:
    coconut=[]
    for digit in data:
        if min_value < digit< max_value:
            coconut.append(digit)
    return coconut
