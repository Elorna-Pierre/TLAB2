import os.path
import glob
from main import run

from config import data1_out, data2_out, data3_out, \
    data4_out, data5_out, data6_out


def assert_equal(result: list, correct: list, name: str) -> None:
    """
    A function to assert correct implementation of functions
    """
    if result == correct:
        print(f"Test {name}: ✅")
    else:
        print(f"Test {name} : ❌")
        print(f"Expected {correct}, got {result}")


def images_present() -> bool:
    """
    A function to check that images with specific filenames
    have been created
    """
    return os.path.isfile("images/averages.png") and\
        os.path.isfile("images/maximums.png") and\
        os.path.isfile("images/stdevs.png")


def delete_images() -> None:
    files = glob.glob('images/*.png')
    for f in files:
        os.remove(f)


if __name__ == "__main__":
    # test correct implementation of basic file
    print("DATA FILE 1 TEST")
    assert_equal(run("data/data1.txt"), data1_out, "Functionality")

    # check image creation
    if images_present():
        print("Image creation: ✅\n")
    else:
        print("Image creation: ❌\n")

    delete_images()

    # test correct implementation of buggy file
    print("DATA FILE 2 TEST")
    assert_equal(run("data/data2.txt"), data2_out, "Functionality")

    # check image creation
    if images_present():
        print("Image creation: ✅\n")
    else:
        print("Image creation: ❌\n")

    delete_images()

    # test correct implementation of file with 1 value
    print("DATA FILE 3 TEST")
    assert_equal(run("data/data3.txt"), data3_out, "Functionality")

    # check image creation
    if images_present():
        print("Image creation: ✅\n")
    else:
        print("Image creation: ❌\n")

    delete_images()

    # test correct implementation of file with 1 blank line
    print("DATA FILE 4 TEST")
    assert_equal(run("data/data4.txt"), data4_out, "Functionality")

    # test correct implementation of file with multiple blank lines
    print("\nDATA FILE 5 TEST")
    assert_equal(run("data/data5.txt"), data5_out, "Functionality")

    # test correct implementation of file with multiple blank lines
    print("\nDATA FILE 6 TEST")
    assert_equal(run("data/data6.txt"), data6_out, "Functionality")

    # check image creation
    if images_present():
        print("Image creation: ✅\n")
    else:
        print("Image creation: ❌\n")

    delete_images()
