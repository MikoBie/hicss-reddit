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
COLORS = ["#E6B830", "#A5C9E6", "#73C0C1"]

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
df = pd.melt(df, id_vars=["Country"], var_name="COMb", value_name="prop").sort_values(
    "prop"
)

# %%
## Plot
plt = hv.Bars(df, vdims=["prop"], kdims=["COMb", "Country"]).opts(
    multi_level=False,
    xlabel="",
    yformatter=mtick.PercentFormatter(),
    color=hv.Cycle(COLORS),
    aspect=1.5,
    show_legend=True,
    yaxis=None,
)

labels = [
    hv.Text(0.02, 0.05, "1%"),
    hv.Text(0.28, 0.09, "5%"),
    hv.Text(0.55, 0.26, "22%"),
    hv.Text(1.02, 0.16, "12%"),
    hv.Text(1.28, 0.21, "17%"),
    hv.Text(1.55, 0.26, "22%"),
    hv.Text(2.02, 0.23, "19%"),
    hv.Text(2.28, 0.29, "25%"),
    hv.Text(2.55, 0.37, "33%"),
    hv.Text(3.02, 0.76, "72%"),
    hv.Text(3.28, 0.64, "60%"),
    hv.Text(3.55, 0.49, "45%"),
]
fig = plt * hv.Overlay(labels)
# %%
hv.output(fig, size=250)
hv.save(fig, PNG / "figure.png", size=250, fmt="png", dpi=200)
