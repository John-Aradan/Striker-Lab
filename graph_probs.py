import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load your data
@st.cache_data
def load_data():
    combined = pd.read_csv('Data/temp.csv')
    uw = pd.read_csv('Data/uw.csv')
    macs = pd.read_csv('Data/macs.csv')
    return combined, uw, macs

combined, uw, macs = load_data()

# Streamlit UI
st.title("Diagnosis Probability vs Ratio")
st.sidebar.header("Visualization Settings")

# Dataset selector
dataset_choice = st.sidebar.selectbox("Choose dataset", ['combined', 'uw', 'macs'])

# Age and Ratio range
age_min, age_max = st.sidebar.slider("Age range", 0, 100, (50, 60))
ratio_min, ratio_max = st.sidebar.slider("Ratio range", 0.0, 4.0, (0.2, 1.4), step=0.05)

# Bin size
bin_size = st.sidebar.slider("Bin size", 0.01, 0.5, 0.1, step=0.01)

# Map dataset string to DataFrame
df_map = {
    'combined': combined,
    'uw': uw,
    'macs': macs
}
df = df_map[dataset_choice]

# Filter and process
df_filtered = df[(df['Ratio'] >= ratio_min) & (df['Ratio'] <= ratio_max)]
df_filtered = df_filtered[(df_filtered['AGEATVIS'] >= age_min) & (df_filtered['AGEATVIS'] <= age_max)]

bins = pd.cut(df_filtered['Ratio'], bins=np.arange(ratio_min, ratio_max + bin_size, bin_size), right=False)
df_filtered = df_filtered.copy()
df_filtered['RatioBin'] = bins

cyt_counts = (
    df_filtered.groupby(['RatioBin', 'CYT_DIAG'], observed=False)
    .size()
    .unstack(fill_value=0)
)

cyt_probs = cyt_counts.div(cyt_counts.sum(axis=1), axis=0)
cyt_probs.sort_index(ascending=False, inplace=True)

# Plot
st.subheader(f"CYT_DIAG Probability vs Ratio for {dataset_choice.upper()}")
fig, ax = plt.subplots(figsize=(12, 6))
for diag in cyt_probs.columns:
    ax.plot(
        cyt_probs.index.astype(str),
        cyt_probs[diag],
        marker='o',
        label=f'DIAG {diag}'
    )

ax.set_xlabel('Ratio Bin')
ax.set_ylabel('Proportion')
ax.set_title(f'Diagnosis Probabilities (Age {age_min}-{age_max})')
ax.tick_params(axis='x', rotation=90)
ax.legend(title='CYT_DIAG')
ax.grid(True)
st.pyplot(fig)