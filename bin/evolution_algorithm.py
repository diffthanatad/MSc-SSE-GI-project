import argparse
import configparser
import pathlib

import magpie


# ================================================================================
# Main function
# ================================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Magpie Evolutionary Algorithm')
    parser.add_argument('--scenario', type=pathlib.Path, required=True)
    parser.add_argument('--algo', type=str)
    parser.add_argument('--seed', type=int)
    args = parser.parse_args()

    # read config file
    config = configparser.ConfigParser()
    config.read_dict(magpie.bin.default_config)
    config.read(args.scenario)

    # select PSO algorithm
    if args.algo is not None:
        config['search']['algorithm'] = args.algo
    if config['search']['algorithm']:
        algo = magpie.bin.algo_from_string(config['search']['algorithm'])
    else:
        config['search']['algorithm'] = 'ParticleSwarmOptimization'
        algo = magpie.algo.ParticleSwarmOptimization

    # setup protocol
    magpie.bin.setup(config)
    protocol = magpie.bin.protocol_from_string(config['search']['protocol'])()
    protocol.search = algo()
    protocol.program = magpie.bin.program_from_string(config['software']['program'])(config)
    protocol.setup(config)

    # run experiments
    protocol.run()
