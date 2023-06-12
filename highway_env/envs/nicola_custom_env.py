"""Custom Highway Environment"""
from highway_env.envs.common.abstract import AbstractEnv
from highway_env.road.road import RoadNetwork
from highway_env.road.lane import StraightLane


class CustomRoadEnv(AbstractEnv):
    def __init__(self):
        super().__init__()

    def get_config(self) -> dict:
        """
        Return the default config
        """
        return self.default_config()

    def _make_road(self):
        nodes: list = [("a", "b"), ("b", "c"), ("c", "d")]
        road_network: RoadNetwork = RoadNetwork()

        for node in nodes:
            lane: StraightLane = StraightLane(start=node[0], end=node[1])
            road_network.add_lane(_from=node[0], _to=node[1], lane=lane)
