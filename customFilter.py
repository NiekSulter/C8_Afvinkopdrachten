import re
from markupsafe import Markup


def reg_replace(string, replace):
    ret = re.sub(re.compile(r"({})".format(replace), flags=re.IGNORECASE),
                 Markup("<b>{}</b>".format(replace)), string)
    return ret
