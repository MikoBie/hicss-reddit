# `A Comparative Analysis of Reddit Discussions on Meat Reduction in Portugal, Poland, and the United Kingdom`

This is a repository for the manuscript on "A Comparative Analysis of Reddit Discussions on Meat Reduction in Portugal, Poland, and the United Kingdom" by Magdalena Roszczyńska-Kurasińska, Mikołaj Biesaga, and Carolina Alves De Oliveria.

## Repo Structure

```bash
├── README.md                      # README
├── notebooks                      # Mostly quarto notebooks
│   └── hicss-reddit.ipynb         # Notebook with data collection description
├── environemnt.yaml               # Necessary modules
└── png                            # Folder with graphics.
```

## Google Colab

Users who want to use the materials online in `Google Colab` should follow these steps to access the interactive notebooks:

1. Go to [www.colab.research.google.com](https://colab.research.google.com/) (it is better to have a Google Account but not necessary).
2. Press GitHub in the popup window or press File and Open notebook.
3. Type `MikoBie` in the search box (compare the picture below).
![github](/png/colab_notebook.png)
4. Pick the relevant repository: `hicss-reddit`
5. Choose the relevant notebook and click Open Notebook.

That is it, an interactive notebook should open.

## Jupyter Notebook App

For more advanced users I recommend running Jupyter Notebooks on their local machines. In the long shot, it is just easier.

### Main Dependencies

* _python3.12_ ([anaconda distribution](https://www.anaconda.com/products/distribution) is preferred)
* other _python_ dependencies are specified in `environemnt.yaml`

### Setup

1. Clone the repo: [git@github.com:MikoBie/hicss-reddit](git@github.com:MikoBie/hicss-reddit)
2. Set up the proper virtual environment.
```bash
cd hicss-reddit
conda env create --file environment.yaml
```
3. Cross fingers and everything should work.

