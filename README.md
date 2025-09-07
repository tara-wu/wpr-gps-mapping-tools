# Walefield Park Raceway GPS Mapping Scripts
This repository contains a set of ArcGIS Pro Python scripts used to convert GPS data from Walefield Park Raceway (WPR) into polyline vector datasets. The scripts support both list-based and dictionary-based processing approaches and share a common module for core functionality.

---

## Contents

| Script                     | Description                                                                 |
|----------------------------|-----------------------------------------------------------------------------|
| `wpr_mapper_lists.py`      | Converts WPR GPS CSV data into polylines using list-based processing. Requires `wpr_mapper_module.py`. |
| `wpr_mapper_dictionaries.py` | Converts WPR GPS CSV data into polylines using dictionary-based processing. Requires `wpr_mapper_module.py`. |
| `wpr_mapper_module.py`     | Shared module containing functions used by both of the above scripts. Must be in the same directory. |

---

## Requirements
- ArcGIS Pro (with Python 3.x and ArcPy)
- GPS data in `.csv` format (e.g., `WPRtrack.csv`)
- All scripts and data must be in the same working directory

---

## Setup
1. Clone or download this repository.
2. Place your GPS data CSV file (e.g., `WPRtrack.csv`) into the same folder as the scripts.
3. Your file structure should look like this:

```plaintext
wpr-gps-mapping-tools/
├── wpr_mapper_lists.py
├── wpr_mapper_dictionaries.py
├── wpr_mapper_module.py
├── WPRtrack.csv  # <-- Your data file
├── README.md
```````

---

## How to Run
<b> Option 1: Using wpr_mapper_lists.py</b>
<b> Option 2: Using wpr_mapper_dictionaries.py</b>

Note: These scripts are designed to be run from ArcGIS Pro’s Python window or the Python Command Prompt with ArcPy available.

---
## Notes
- Both wpr_mapper_lists.py and wpr_mapper_dictionaries.py require wpr_mapper_module.py in the same directory.
- Make sure your input CSV file uses the correct GPS data format expected by the scripts

