from pathlib import Path
import numpy as np


# Download temperature dataset
url = "http://berkeleyearth.lbl.gov/auto/Global/Land_and_Ocean_summary.txt"
data = np.loadtxt(url, comments="%")

# Read reference temperature from header
file_path = Path(".")
for part in url[7:].split("/"):
    file_path /= part
with open(file_path, "r") as f:
    for line in f:
        if "Using air temperature above sea ice:" in line:
            reference_temp = float(line.split()[-3])
            break

# Read data
years = data[:, 0].astype(int)
temperature_anual = data[:, 1] + reference_temp

# Save data to file
outfile = Path(__file__).parent / "temperature-berkeley.dat"
header = "# Earth's global average surface temperature in Celsius.\n"
header += "# Source: Berkeley Earth\n#\n"
header += "# Year   Temperature [C]\n"

with open(outfile, "w") as f:
    f.write(header)
    for year, temp in zip(years, temperature_anual):
        f.write(str(year) + " " + str(temp) + "\n")
