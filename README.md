# Project Directory Structure

The project is organized as follows:

```
PFDA-programming-for-data-analytics/
├── README.md
├── requirements.txt
├── assignments/
│   ├── assignment02-bankholidays.py
│   ├── assignment02-bankholidays.txt
|   ├── assignment03-pie.ipynb
|   ├── assignment05-population.ipynb
|   └── assignment_6_Weather.ipynb
├── data/
│   └── README.md
├── data/
│   └── bankholidays.json
├── my-work/
└── project/
```

# ATU Programing for data analytics 2025/6
ATU - programming-for-data-analytics 2025/6

## Python Environment Setup

To set up your Python environment for this project:

1. **Create a virtual environment** (recommended):

	Open a terminal in the project root and run:
   
	```powershell
	python -m venv .venv
	```

2. **Activate the environment**:

	On PowerShell (Windows):
	```powershell
	. .venv\Scripts\Activate
	```

	On Command Prompt (Windows):
	```cmd
	.venv\Scripts\activate.bat
	```

	On macOS/Linux:
	```bash
	source .venv/bin/activate
	```

3. **Install requirements**:

	```powershell
	pip install -r requirements.txt
	```

Your environment is now ready to use. Run scripts with:

```powershell
python your_script.py
```

## Assignments

### Assignment 02 - Northern Bank Holidays

Write a program called `assignment02-bankholidays.py` that prints out the dates of the bank holidays that happen in Northern Ireland.

**Challenge**: Modify the program to print the bank holidays that are unique to Northern Ireland (i.e. do not happen elsewhere in the UK). You can choose if you want to use the name or the date of the holiday to decide if it is unique.

**Files:**
- `assignments/assignment02-bankholidays.py` - code
- `assignments/assignment02-bankholidays.txt` - output of run

### Assignment 03 - Email Domains Pie Chart

Create a notebook called `assignment03-pie.ipynb` that contains a nice pie chart of people's email domains from the CSV file at:

https://drive.google.com/uc?id=1AWPf-pJodJKeHsARQK_RHiNsE8fjPCVK&export=download

This CSV file has 1000 people. You may download the data or link to it.

**Files:**
- `assignments/assignment03-pie.ipynb` - code jupyter notebook

### Assignment 05 - Population Analysis

Analyse the differences between the male and female population by age in Ireland.

**Part 1 (70%)**:
- Calculate weighted mean age by sex
- Analyse the difference between the sexes by age
- This part does not need to look at the regions

**References:**
- https://data.cso.ie/
- https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FY006A/CSV/1.0/en

**Files:**
- `assignments/assignment05-population.ipynb` - code jupyter notebook

### Assignment 06 - Weather Data Analysis

Create a notebook called `assignment_6_Weather.ipynb` using data from:

https://cli.fusio.net/cli/climate_data/webdata/hly4935.csv

**Part 1 (60%)** - Plot:
- The temperature
- The mean temperature each day
- The mean temperature for each month

**Part 2 (40%)** - Plot:
- The windspeed (note: data missing from this column)
- The rolling windspeed (over 24 hours)
- The max windspeed for each day
- The monthly mean of the daily max windspeeds

**Files:**
- `assignments/assignment_6_Weather.ipynb` - code jupyter notebook


