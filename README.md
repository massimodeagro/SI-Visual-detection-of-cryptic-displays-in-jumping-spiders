Supplemental information for "Visual detection of cryptic displays in jumping spiders"

DOI to preprint available soon

## Content:

### SI1 - analysis
files reporting the analysis done in R.
- `SI1_analysis.html` visible through github pages

### SI2 - data
files containing the raw data for the analysis
- `SI2_data_exp_1_2.csv` contains data for experiment 1 and 2. these are distinguishable by date, see `SI1_analysis.html`
- `SI2_data_exp_3.csv` contains data for experiment 3 (selective eye showing)

### SI3 - spatiotemporal filter model
files describing the filter generation
- `SI3_stimuliGeneration.py` contains the code used to generate the numpy matrices of the visual stimuli
- `SI3_spatiotemporal_filter_model.py` this implements the spatiotemporal filter, applies it to the stimuli and generate a binary response, repeating many times until getting simulated experiment

### SI4 - plot
this is for Figure 3 generation
- `SI4_data_to_plot.csv` organized model output (from SI1) and simulated output (SI3) data for plot
- `SI4_plot.py` code that generates the plot from data
