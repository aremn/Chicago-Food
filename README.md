# Chicago Food Inspections Analysis

## Project Overview

This project focuses on the analysis and predictive modeling of food inspection data from the city of Chicago. The dataset comprises various details about each inspection, such as the facility type, address, risk level, violations found, and the final results of the inspection. The primary aim is to build a robust predictive model that can accurately determine the factors influencing the inspection results.

## Table of Contents

- [Project Overview](#project-overview)
- [Installation](#installation)
- [Usage](#usage)
- [Results](#results)
- [Future Work](#future-work)

## Installation

The primary requirements for this project are Python 3.x and Jupyter Notebook. The project also uses several Python libraries like pandas, numpy, matplotlib, and sklearn. These can be installed via pip:

```
pip install pandas numpy matplotlib sklearn
```

## Usage

To run the project, open the Jupyter Notebook file `project_milestone2.ipynb` in Jupyter Notebook and execute the cells in order.

## Results

The project revealed that the 'Violation Codes' feature was consistently the most important feature across all the models trained. Other important features included 'Inspection Type', 'nb_violation', 'Inspection Year', and 'Distance to City Center'. The predictive performance of the models was significantly improved by the engineered features.

## Future Work

The upcoming stages of this project include:

- **Analysis of Violation Codes**: The 'Violations' column, containing codes and descriptions of violations found during inspections, will be further analyzed. The aim is to categorize these codes into larger groups, facilitating a better understanding and easier visualization.
- **Geographic Analysis**: The inspections will be analyzed on a neighborhood basis to potentially identify patterns or trends.
- **Trends Over Time**: The changes in restaurants' inspection scores over time will be investigated.
- **Connection to Geodemographic Characteristics**: The relationship between inspection results and the Life Quality Index of the area will be explored.
- **Connection to Customer Reviews**: The correlation between inspection results and customer reviews will be examined.
