import pytest

@pytest.mark.parametrize("username, password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("admin", "admin123")
])
def test_login(username, password):
    assert login(username, password) == "Success"

    import pytest

    @pytest.fixture(params=["chrome", "firefox", "safari"])
    def browser(request):
        return request.param

    def test_browser(browser):
        assert browser in ["chrome", "firefox", "safari"]



