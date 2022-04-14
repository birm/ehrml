import ehrml

def test_nothing():
    assert 0==0

# test the rwb utility
def test_fromRwb():
    data = {'constant': 1, 'hunger_00_08': 100, 'hunger_08_16': 50}
    configuration = [{'rwb_src': 'constant'}, {'rwb_src': 'hunger'}]
    res = ehrml.fromRwb(configuration, data, time_limit=2)
    print(res)
    assert len(res) == 4
