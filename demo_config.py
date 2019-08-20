import yaml

from easydict import EasyDict as edict

def Config(filename):
    with open(filename, "r") as f:
        parser = edict(yaml.load(f))
        print(parser)

    for x in parser:
        print('{}:{}'.format(x, parser[x]))
   
    return parser

    
parser = Config("config.yml")
print(parser.a, parser['a'])