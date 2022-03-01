import csv
import datetime
import subprocess



def make_measurements(file_prefix, number_of_samples=60, interval=1):
    filename =  file_prefix + str(datetime.datetime.now()) + ".csv"
    print("I am here")
    try:
        process = subprocess.check_output(["powerstat", "-D", str(interval), str(number_of_samples)], timeout=70, text=True)
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            header = process.strip().split("\n")[3].split()
            measurement_values = process.strip().split("\n")[4:4+number_of_samples]
            writer.writerow(header)
            for value in measurement_values:
                writer.writerow(value.split())
            return True
    except Exception as e:
        print("Exception happened: %s" % e)
        return False