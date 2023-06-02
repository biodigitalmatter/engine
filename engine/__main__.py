import argparse
from engine.agent import create_agents
from engine.world_backends.openvdb import OpenVDBBackend
from engine.world import World


def engine(number_of_agents, time_steps):
    agents = create_agents(number_of_agents)

    world = World(OpenVDBBackend)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number_of_agents", type=int)
    parser.add_argument("time_steps", type=int)
    args = parser.parse_args()

    engine(args.number_of_agents, args.time_steps)
