from compas.geometry import Point, Vector


class Agent:
    def __init__(self, agent_id):
        self.id = agent_id
        self.location = Point(0, 0, 0)

    def walk(self, vector: Vector):
        self.location += vector


def create_agents(num_agents):
    return [Agent(i) for i in range(num_agents)]
