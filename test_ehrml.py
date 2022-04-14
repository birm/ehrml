import ehrml

def test_nothing():
    assert 0==0

# test the flat with time utility
def test_fromFlat():
    data = {'constant': 1, 'hunger_00_08': 100, 'hunger_08_16': 50}
    # minimal configuration, all which is needed for this test
    configuration = [{'rwb_src': 'constant'}, {'rwb_src': 'hunger'}]
    res = ehrml.fromFlat(configuration, data, time_limit=2)
    print(res)
    assert len(res) == 4

# test the api utility
def test_fromLayered():
    pass
