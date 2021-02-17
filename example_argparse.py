import argparse


parser = argparse.ArgumentParser()

parser.add_argument('--config', help='Specify the full path to the config file')


cmd_pars = parser.parse_args()
print(cmd_pars.config)
