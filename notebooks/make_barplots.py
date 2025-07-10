# %%
## Libraries
import holoviews as hv
from pathlib import Path
import matplotlib.ticker as mtick
import pandas as pd

hv.extension("matplotlib", logo=False)

# %%
## Globals
ROOT = Path(__file__).absolute().parent.parent
PNG = ROOT / "png"
COLORS = ["#FFFFFF","#E6B830",  "#73C0C1","#A5C9E6", ]

# %%
## Data
df = pd.DataFrame(
    {
        "Capabilities": [0.22, 0.01, 0.05],
        "Opportunities": [0.22, 0.12, 0.17],
        "Motivations": [0.33, 0.19, 0.25],
        "Empty": [0.45, 0.72, 0.6],
        "Country": ["Poland", "Portugal", "United Kingdom"],
    }
)
df = pd.melt(df, id_vars=["Country"], var_name="COM-B", value_name="prop").sort_values(
    "prop", ascending=True
)

# %%
## Plot
plt = hv.Bars(df, vdims=["prop"], kdims=["Country", "COM-B"]).opts(
    multi_level=False,
    xlabel="",
    yformatter=mtick.PercentFormatter(),
    color=hv.Cycle(COLORS),
    aspect=1.5,
    show_legend=True,
    yaxis=None,
)

labels = [
    hv.Text(0, 0.74, "72%"),
    hv.Text(1, 0.62, "60%"),
    hv.Text(2, 0.47, "47%"),
    hv.Text(0.225, 0.21, "19%"),
    hv.Text(1.225, .27, "25%"),
    hv.Text(2.225, .35, "33%"),
    hv.Text(0.425, 0.14, "12%"),
    hv.Text(1.425, .19, "17%"),
    hv.Text(2.425, .24, "22%"),
    hv.Text(0.62, 0.03, "1%"),
    hv.Text(1.62, .07, "5%"),
    hv.Text(2.62, .24, "22%"),
]
fig = plt * hv.Overlay(labels)
# %%
hv.output(fig, size=250)
hv.save(fig, PNG / "figure.png", size=250, fmt="png", dpi=200)
