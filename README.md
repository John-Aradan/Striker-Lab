# Striker-Lab

## Purpose

This project provides a tool to **visualize how the probability of a patient belonging to one of four classes**—Normal, LSIL, HSIL, and Cancer—varies as specific features change over time. The main feature of interest demonstrated is how the probability distribution across these classes evolves as the "Ratio" feature of a patient decreases.

## Features

- **Class Probability Visualization**: See how the likelihood of a patient falling into each diagnostic class (Normal, LSIL, HSIL, Cancer) changes with the patient's feature values, especially as the Ratio decreases over time.
- **Dataset Selection**: Choose between three datasets for analysis:
  - `uw`
  - `macs`
  - `combined`
- **Flexible Feature Ranges**:
  - Specify custom ranges for both patient age and the Ratio feature.
- **Adjustable Bucket Size**:
  - Change the bucket size for Ratio to control the granularity of the visualization.

## Usage

1. **Select Dataset**: Choose from `uw`, `macs`, or `combined` datasets depending on your analysis needs.
2. **Set Ranges**:
   - Input the desired age range for patients.
   - Input the desired range for the Ratio feature.
3. **Adjust Bucket Size**: Change the Ratio bucket size for optimal visualization clarity.
4. **Visualize**: View how the probabilities for each class shift as the Ratio changes (typically decreases) within your specified parameters.

## Example Use Case

Suppose you want to understand how the risk profile for cancer develops as a patient's Ratio decreases, specifically for patients aged 40-60, using data from the `combined` dataset. You would:
- Select the `combined` dataset.
- Set the age range to 40–60.
- Set your preferred Ratio range.
- Adjust the Ratio bucket size for clearer or more granular visual output.
- Run the visualization to observe the probability trends across the four classes.

## Requirements

- Python (see environment file or requirements.txt if available)
- Standard scientific/data visualization libraries (e.g., numpy, pandas, matplotlib/seaborn/plotly)

## Getting Started

1. Clone this repository:
    ```bash
    git clone https://github.com/John-Aradan/Striker-Lab.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the visualization tool (see script or notebook for exact entry point).


**Note:** If you have further questions or need more detailed instructions, please refer to the code comments or open an issue in this repository.
