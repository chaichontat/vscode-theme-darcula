#%%
import json
import colorsys
from pathlib import Path
import numpy as np
from pprint import pprint
from colour import Color
import copy

# %%

s = json.loads(
    Path("/Users/chaichontat/Downloads/vscode-theme-darcula/themes/darculaori.json").read_text()
)
ori = copy.deepcopy(s)

out = ""


def run(d):
    global out
    if isinstance(d, list):
        for k in d:
            if isinstance(k, dict):
                run(k)

    else:
        for k, v in d.items():
            if isinstance(v, dict) or isinstance(v, list):
                run(v)
            if isinstance(v, str) and v.startswith("#"):
                # v = v.lstrip("#")
                c = Color(v[:7])
                out += c.get_hex_l()
                if 0 < c.saturation < 1:
                    if c.luminance > 0.3:
                        c.luminance = np.clip(c.luminance + 0.1, 0, 1)
                        if c.saturation > 0:
                            c.saturation = np.clip(c.saturation + 0.2, 0, 1)
                elif c.saturation == 0:
                    if c.luminance > 0.5:
                        c.luminance = np.clip(c.luminance + 0.2, 0, 1)
                else:
                    ...
                    # c.luminance = np.clip(c.luminance + 0.05, 0, 1)

                # out = (
                #     "#"
                #     + "".join([format(int(v), "02x") for v in colorsys.hls_to_rgb(*u)])
                #     + v[6:]
                # )
                out += "\t" + c.get_hex_l() + "\n"
                d[k] = c.get_hex_l() + v[7:]
                # print(v, out)
                # d[k] = colorsys.hsv_to_rgb(*u)


# pprint(s)
run(s)
Path("/Users/chaichontat/Downloads/vscode-theme-darcula/themes/darcula.json").write_text(
    json.dumps(s)
)
Path("/Users/chaichontat/Downloads/vscode-theme-darcula/themes/comp.txt").write_text(out)
# %%
s
# %%
