# bin observations
import datetime
import math
from .utils import readTime, truthy_values

def binObs(config, observations, numBins, binLength, now=None):
    res = []
    keyedConf = {x.get('rwb_src'): x for x in config}
    # for each bin time range
    # set "now" to the end of the current time range
    set_hour = (binLength * (math.floor(datetime.datetime.now().hour/binLength)+1))
    now = now or datetime.datetime.now().replace(hour=int(set_hour), minute=0, second=0, microsecond=0)
    ranges = [(now + datetime.timedelta(hours=i*binLength), now + datetime.timedelta(hours=(i+1)*binLength)) for i in range(0-numBins, 0)]
    for r in ranges:
        range_res = {}
        # grab all observations in this time
        ranged_obs = [x for x in observations if x.get('time') and x['time'] > r[0] and x['time'] < r[1]]
        for c in keyedConf:
            relevant_obs = [x for x in ranged_obs if x.get('field') and x['field'] == c]
            # for each in conf, use conf to determine how to reduce
            if keyedConf[c].get('transformation') == "binary":
                # if any are true, it's true (assuming anything binary, seen with no value is true)
                if set([x.get('value', True) for x in relevant_obs]).intersection(set(truthy_values)):
                    range_res[c] = True
                else:
                    range_res[c] = False
            else:
                if len(relevant_obs) == 0:
                    # use explicit None to denote missing
                    range_res[c] = None
                else:
                    range_res[c] = max(relevant_obs, key= lambda k: k['time'])['value']
        res.append(range_res)
    return res
