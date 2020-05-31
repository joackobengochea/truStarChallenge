# python get_info.py --repo-id=mitre/cti --folder=enterprise-attack/attack-pattern
# --out=parsed_data.json --access-token=baeb03eff471a78a9c1700d1026ffa4f05089f10
import argparse
import json

from lib.github import GithubManager
from lib.parser import get_attributes


if __name__ == "__main__":
    argument_parser = argparse.ArgumentParser()
    argument_parser.add_argument('--repo-id', default='mitre/cti', help='id of the repo to extract info from')
    argument_parser.add_argument('--folder', default='enterprise-attack/attack-pattern',
                                 help='folder where the json files are')
    argument_parser.add_argument('--access-token', help='Github access token', required=True)
    argument_parser.add_argument('--out', default='parsed_data.json', help='path of the output file')
    argument_parser.add_argument('--fields', default='id,objects[0].name,objects[0].kill_chain_phases',
                                 help='fields to extract from the repo files')
    args = argument_parser.parse_args()

    github_manager = GithubManager(args.access_token)
    jsons_to_parse = github_manager.get_json_strings(args.repo_id, args.folder)
    fields = args.fields.split(',')
    results = [get_attributes(json_str, fields) for json_str in jsons_to_parse]
    json_result = json.dumps(results)
    with open(args.out, 'w') as out_file:
        out_file.write(json_result)
