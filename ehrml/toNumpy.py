# condert data into the expected numpy format
import numpy

def _locf_impute(data):
    if data[0] is None:
        data[0] = 0
    data = [x if x is not None else data[i-1] for i, x in enumerate(data)]
    return data


def _none_impute(data):
    return data

_imputation_options = {'none':_none_impute, 'locf': _locf_impute}

def toNumpyRecord(config, data, shape, impute="locf"):
    res = numpy.zeros(shape)
    for c in config:
        d = [x.get(c.get('rwb_src'), None) for x in data]
        # expand one hots
        if type(d[0]) is list:
            for i in range(len(d)):
                if d[i]:
                    for j in range(len(d[i])):
                        res[i, int(c.get('index')) + j] = d[i][j]
        else:
            # set missing flags
            if c.get('missing_flag_index'):
                res[:, int(c.get('missing_flag_index'))] = [1 if x is None else 0 for x in d]
            # impute
            d = _imputation_options[impute](d)
            # set results in res
            res[:, int(c.get('index'))] = d
    return res

def numpyRecordCollector(records):
    x, y = records[0].shape
    res = numpy.zeros((len(records), x, y))
    for i in range(len(records)):
        res[i, :, :] = records[i]
    return res
