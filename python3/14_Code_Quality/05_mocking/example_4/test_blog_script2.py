from unittest import TestCase
from unittest.mock import patch

import blog_script


class TestBlog(TestCase):
    @patch("blog_script.Blog")
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value = [
            {
                "userId": 1,
                "id": 1,
                "title": "Test Title",
                "body": r"Far out in the uncharted backwaters of the unfashionable  end  of the  western  spiral  arm  of  the Galaxy\ lies a small unregarded yellow sun.",
            }
        ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0], dict)

        # Additional assertions
        assert MockBlog is blog_script.Blog  # The mock is equivalent to the original

        assert MockBlog.called  # The mock wasP called

        blog.posts.assert_called_with()  # We called the posts method with no arguments

        blog.posts.assert_called_once_with()  # We called the posts method once with no arguments

        # blog.posts.assert_called_with(1, 2, 3) - This assertion is False and will fail since we called blog.posts with no arguments

        blog.reset_mock()  # Reset the mock object

        blog.posts.assert_not_called()  # After resetting, posts has not been called.
