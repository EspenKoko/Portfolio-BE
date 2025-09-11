class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
        
    def test_three(self):
        x = "hello"
        assert hasattr(x, "upper")
        
    def test_four(self):
        x = {"foo": "bar"}
        assert "bar" in x.values()
        
    def test_five(self):
        x = {"foo": "bar"}
        assert "foo" in x