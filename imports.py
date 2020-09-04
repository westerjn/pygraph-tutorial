import math
import numpy as np
import pandas as pd

from bokeh.embed import components
from bokeh.models import ColumnDataSource, HoverTool, PrintfTickFormatter
from bokeh.plotting import figure
from bokeh.transform import factor_cmap

from flask import Flask, render_template, request

df = pd.read_csv('../data/titanic.csv')
df['Title'] = df['Name'].apply(lambda x: x.split(',')[1].strip().split(' ')[0])