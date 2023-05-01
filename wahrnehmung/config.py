import yaml

def parse_config():
    with open('wahrnehmung/config.yml', 'r') as f:
        return yaml.safe_load(f)