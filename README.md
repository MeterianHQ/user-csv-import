# user-csv-import
Simple script to enable admins to fill their Meterian account by using a csv list of users

## Usage
Run the command
`pipenv run python bin/run.py --input=/path/to/input.csv --meterian-token=$METERIAN_API_TOKEN`
also `--token=$METERIAN_API_TOKEN` is an accepted parameter

**The token used MUST be an Administration token (the user linked to the token is an Administrator of the account)**

## The CSV List

In the csv list indicate
- Full name;
- Email address;
- Role within the team;
- Team name

Example:
```
John Doe,jon.doe@meterian.uk,Viewer,UK
Kate Middleton,kate@meterian.uk,Administrator,UK
```
