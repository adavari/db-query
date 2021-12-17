import json
import csv


def write_output(output_answer: dict, response: list):
    out_format = output_answer['output_format']
    path = output_answer['output_path']
    with open(path, 'w') as out_file:
        if out_format == 'csv':
            writer = csv.writer(out_file, delimiter='"', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for row in response:
                writer.writerow(row.values())
        else:
            json.dump(response, out_file)
