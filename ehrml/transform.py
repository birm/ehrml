import math

from .utils import truthy_values

# binary transformations
def _binary(value, one_hot_vals):
    return 1.0 if value in truthy_values else 0.0

def _cutoffs(value, one_hot_vals):
    pass

def _categorical(value, one_hot_vals):
    pass

# numeric transformations
def _zScore(value, mean, std, max, min):
    return (value - mean) / std

def _high(value, mean, std, max, min):
    return ((max - value + 1)- mean) / std

def _low(value, mean, std, max, min):
    return ((value - min + 1)- mean) / std

def _sqrtHigh(value, mean, std, max, min):
    return (math.sqrt(max - value + 1) - mean) / std

def _sqrtLow(value, mean, std, max, min):
    return (math.sqrt(value - min + 1) - mean) / std

def _logHigh(value, mean, std, max, min):
    return (math.log(value - min + 1) - mean) / std

def _logLow(value, mean, std, max, min):
    return (math.log(max - value + 1) - mean) / std

_bin_tx = {'binary': _binary, 'cutoffs': _cutoffs, 'categorical': _categorical}
_num_tx = {'z': _zScore, 'low': _low, 'high': _high, 'sqrt low': _sqrtLow, 'sqrt high': _sqrtHigh, 'log low': _logLow, 'log high': _logHigh}

def transform(config, binnedData):
    res = []
    keyedConf = {x.get('rwb_src'): x for x in config}
    for b in binnedData:
        bRes = {}
        for c in keyedConf:
            if c.get('transformation', 'none') in _bin_tx:
                # TODO -- how to use, handle
                bRes[c] = _bin_tx(b[c], c.get('one_hot_vals'))
            elif c.get('transformation', 'none') in _num_tx:
                bRes[c] = _num_tx(b[c], float(c.get('mean')), float(c.get('std')), float(c.get('max')), float(c.get('min')))
        res.append(bRes)
    return res
