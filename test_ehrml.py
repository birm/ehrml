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
    time1 = "2022-01-01T00:00:01"
    time2 = "2022-01-01T12:00:01"
    data = {'basic':[{'hunger':100, 'time':time1}, {'hunger':10, 'time':time2}],
            'deep':[{'field':'ignore', 'value':-1, 'time':time1}, {'field':'thirst', 'value': 45, 'time':time1}, {'field':'thirst', 'value': 15, 'time':time2}]}
    configuration = [{'rwb_src':'hunger', 'api_parent':'basic', 'api_time_src':'time', 'api_src':'hunger'},
                     {'rwb_src':'thirst', 'api_parent':'deep', 'api_time_src':'time', 'api_by':'field', 'api_from':'value', 'api_src':'thirst'}]
    res = ehrml.fromLayered(configuration, data)
    print(res)
    assert len(res) == 4
