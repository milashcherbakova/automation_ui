def test_first_try():
    print("Hello World!")


def test_assert_positive_case():
    assert (2 + 2) == 4


def test_assert_negative_case():
    assert (2 + 2) == 5

    import pytest

    @pytest.mark.regression
    class TestUserAuthentication:

        @pytest.mark.smoke
        def test_login(self):
            pass

        @pytest.mark.slow
        def test_password_reset(self):
            pass

        def test_logout(self):
            pass
