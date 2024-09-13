# PDF to Excel :snake:

Convert **PDF** to **Excel**, read all data of PDF and return excel file with this data

## Run

**The script need two arguments**:

***first  argument***: is the `dir where PDF files are`.

***second argument***: is where the script `save the output Excel files`.

```bash
  py main.py /source/pdf/path /final/excel/path
```

## Versions

```bash
 py --version
 v3.10.5
 Output:

 pip --version
 Output: pip 24.2
```

## Dependcies/Libaries

You need install the the next libraries:

1. **pandas** - Manage Excel
2. **tabula-py** - Convert/Read PDF
3. **JPype1** - Is necesary for tabula-py

### Install

Run this command from cmd/bash:

```bash
  pip install JPype1 tabula-py pandas
```
