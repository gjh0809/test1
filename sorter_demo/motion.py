from dataclasses import dataclass
import random

from .models import Pose


@dataclass
class Trajectory:
    grasp_pose: Pose
    target_lane: str


class MotionService:
    """Mock motion planner and executor."""

    def __init__(self, plan_success_rate: float = 0.95, exec_success_rate: float = 0.97):
        self.plan_success_rate = plan_success_rate
        self.exec_success_rate = exec_success_rate
        self.current_traj: Trajectory | None = None

    def plan(self, grasp_pose: Pose, lane: str) -> bool:
        if random.random() > self.plan_success_rate:
            return False
        self.current_traj = Trajectory(grasp_pose=grasp_pose, target_lane=lane)
        return True

    def execute(self) -> bool:
        if not self.current_traj:
            return False
        if random.random() > self.exec_success_rate:
            # 清空当前规划，避免失败后残留的轨迹污染后续状态
            self.current_traj = None
            return False
        # In a real system, execute trajectory, vacuum control, and placement.
        self.current_traj = None
        return True

