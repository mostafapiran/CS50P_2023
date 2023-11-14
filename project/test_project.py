import project


def test_analyze_sentiment():
    assert project.analyze_sentiment("hi") == "Neutral"

def test_factorial():
    assert project.factorial(5) == 120

def test_add_password():
    assert project.add_password("ali","1234") == "Password added for: ali"

def test_view_password():
    assert project.view_password("mostafa") == "Password not found for: mostafa"

