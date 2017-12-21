import argparse

parser = argparse.ArgumentParser(description='Sample code for python.')
parser.add_argument('--username')
parser.add_argument('--query-id', help='Query id to export')
parser.add_argument('--query-api-key', help='API key for the query')

args = parser.parse_args()

print(args.username)
print(args.query_id)
print(args.query-api-key)

