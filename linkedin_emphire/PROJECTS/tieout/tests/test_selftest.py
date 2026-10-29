from tieout.selftest import selftest


def test_selftest_7_of_7():
    passed, total, results = selftest()
    assert total == 7
    assert passed == 7, [
        f"{name}: {detail}" for name, ok, detail in results if not ok
    ]
