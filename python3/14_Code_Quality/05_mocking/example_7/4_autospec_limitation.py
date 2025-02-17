from unittest import TestCase, main
from unittest.mock import Mock, patch


class Foo:
    def __init__(self):
        x = 20  # noqa: F841

    def bar(self):
        pass


class TestFoo(TestCase):
    @patch("__main__.Foo", autospec=True)
    def test_bar(self, mock_foo):
        f = mock_foo()
        # f.x    # AttributeError
        f.x = 20  # solution


# NOTE: autospec can't recognize dynamically
# created objects/attributes

if __name__ == "__main__":
    main()
