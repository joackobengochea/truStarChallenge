# truStarChallenge

# Information extraction from Git Repository

##Installation

This repo works with pipenv, to install the virtual environment run:
```
pipenv shell
pipenv install -r requirements.txt
```

## Usage

Run the script with the following arguments:

`--repo-id`: ID of the repository. Default: mitre/cti
`--folder`: Folder where the json files are. Default: enterprise-attack/attack-pattern
`--access-token`: Github access token. This argument is required. (This access token may be used: baeb03eff471a78a9c1700d1026ffa4f05089f10)
`--out`: path of the output json file. Default: parsed_data.json
`--fields`: list of comma separated fields to parse from the repo files. Default: 'id,objects[0].name,objects[0].kill_chain_phases'

## Tests

To run the tests execute the following command from the root folder:
```
pytest tests
```


**5- Reflecting on the technical spec you received as part of the questionnaire, how would you
change it to make it less error prone (you're being asked to parse a property chain... is this the
best way of doing it?)? Feel free to propose alternatives, listing pros and cons**

I think the questionnaire could begin with the 4th Point, this way the first questions have some context about how the functions will be used. 