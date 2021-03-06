import click
import json

@click.command()
@click.option("--input_file", required=True, type=click.File("rb"), nargs=1)
@click.option("--fields_to_track", type=click.STRING, multiple=True)
@click.option("--fields_to_exclude", type=click.STRING, multiple=True)
def cli(input_file, fields_to_track, fields_to_exclude):
    data = json.load(input_file)
    res = []
    for state_data in data["mortgageRateList"]:
        fields_empty = []
        for state_name in state_data:
            fields = []
            if len(fields_to_track) == 0:
                for k in state_data[state_name]:
                    fields.append(k)
            else:
                fields = fields_to_track

            # Removes fields from the track
            for f in fields_to_exclude:
                fields.remove(f)

            fields_empty = check_fields_empty(fields, state_data[state_name])

        if fields_empty:
            res.append({state_name: fields_empty})
    print(res)


def check_fields_empty(fields_to_track, obj):
    res = []
    for f in fields_to_track:
        if f in obj and number(obj[f]) <= 0.0:
            res.append(f)
    return res

def number(s):
    try:
        return float(s)
    except ValueError:
        return 0.0
