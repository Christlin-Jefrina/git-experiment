from pathlib import Path
def test_output():
    text = Path("result.txt").read_text()
    assert "Job completed" in text
    print("TEST PASSED")
test_output()
