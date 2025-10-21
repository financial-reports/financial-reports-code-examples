# Example: Browse ISIC Hierarchy

This script demonstrates how to use the four ISIC endpoints (`/isic-sections/`, `/isic-divisions/`, `/isic-groups/`, `/isic-classes/`) to explore the classification hierarchy.

The script is interactive. You can list all top-level sections and then "drill down" to see the children of a specific classification.

## Setup

1.  Install the required Python package:
    ```bash
    pip install -r requirements.txt
    ```

## Authentication

This script requires your FinancialReports API key. Set it as an environment variable.

```bash
# On macOS / Linux
export FR_API_KEY="your_api_key_here"
```

## Run

The script accepts several arguments to navigate the hierarchy.

### 1. List all top-level Sections (Level 1):

```bash
python browse_isic.py --list-sections
```

**Expected Output:**

```
Fetching all ISIC Sections...
Found 22 total Sections:
--------------------------------------------------
- [A] Agriculture, forestry and fishing
- [B] Mining and quarrying
- [C] Manufacturing
... (and so on)
```

### 2. List all Divisions (Level 2) within a specific Section:

```bash
python browse_isic.py --list-divisions-in-section C
```

**Expected Output:**

```
Fetching ISIC Divisions for Section 'C'...
Found 24 total Divisions:
--------------------------------------------------
- [10] Manufacture of food products
- [11] Manufacture of beverages
- [12] Manufacture of tobacco products
- [13] Manufacture of textiles
- [14] Manufacture of wearing apparel
... (and so on)
```

### 3. List all Groups (Level 3) within a specific Division:

```bash
python browse_isic.py --list-groups-in-division 14
```

**Expected Output:**

```
Fetching ISIC Groups for Division '14'...
Found 2 total Groups:
--------------------------------------------------
- [141] Manufacture of wearing apparel, except fur apparel
- [142] Manufacture of articles of fur
... (and so on)
```

### 4. List all Classes (Level 4) within a specific Group:

```bash
python browse_isic.py --list-classes-in-group 141
```

**Expected Output:**

```
Fetching ISIC Classes for Group '141'...
Found 1 total Classes:
--------------------------------------------------
- [1410] Manufacture of wearing apparel, except fur apparel
```