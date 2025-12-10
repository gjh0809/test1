"""Sorter demo package with simplified vision, planning and control stubs."""

from .models import Pose, Detection, GraspCandidate
from .handeye import HandEye
from .planner import GraspPlanner, map_lane
from .vision import VisionService
from .motion import MotionService
from .state_machine import StateMachine
from .pipeline import SorterPipeline

__all__ = [
    "Pose",
    "Detection",
    "GraspCandidate",
    "HandEye",
    "GraspPlanner",
    "map_lane",
    "VisionService",
    "MotionService",
    "StateMachine",
    "SorterPipeline",
]

