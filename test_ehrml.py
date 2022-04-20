import ehrml

import datetime
import math

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

# test the observaton bin and reduction logic
def test_binObs():
    override_now = datetime.datetime(2022, 1, 2, 0, 0, 0)
    time1 = datetime.datetime(2022, 1, 1, 14, 0, 0)
    time2 = datetime.datetime(2022, 1, 1, 15, 0, 0)
    time3 = datetime.datetime(2022, 1, 1, 23, 0, 0)
    config = [{'rwb_src': 'binary', 'transformation' : 'binary'},
              {'rwb_src':'missing', 'transformation':'none'},
              {'rwb_src':'frequent', 'transformation': 'none'}]
    observations = [
        {'time': time1, 'value': True, 'field': 'binary'},
        {'time': time2, 'value': False, 'field': 'binary'},
        {'time': time1, 'value': 1., 'field': 'frequent'},
        {'time': time2, 'value': 2., 'field': 'frequent'},
        {'time': time3, 'value': 3., 'field': 'frequent'}]
    res = ehrml.binObs(config, observations, 2, 8.0, now=override_now)
    assert res[0].get('binary')
    assert res[0].get('missing') is None
    assert res[0].get('frequent') == 2
    assert res[1].get('binary') == False
    assert res[1].get('missing') is None
    assert res[1].get('frequent') == 3

# test the transformation
def test_transform():
    config = [{'rwb_src': 'binary', 'transformation' : 'binary'},
              {'rwb_src':'missing', 'transformation':'z', 'mean': 1, 'std':1, 'max':2, 'min':0},
              {'rwb_src':'frequent', 'transformation': 'log high', 'mean': math.e, 'std':1, 'max':math.e, 'min':0}]
    binnedData = [{'binary': True, 'frequent': 1.0, 'missing': None}, {'binary': False, 'frequent': math.e, 'missing': None}]
    res = ehrml.transform(config, binnedData)
    print(res)
    assert res[0].get('binary') == 1.0
    assert res[1].get('binary') == 0.0
    assert res[0].get('missing') is None
    assert res[1].get('missing') is None
    assert res[0].get('frequent') == -math.e + 1
    assert res[1].get('frequent') == -math.e
