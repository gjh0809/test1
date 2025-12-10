import unittest
from unittest.mock import patch

from sorter_demo import MotionService, Pose


class MotionServiceTests(unittest.TestCase):
    def test_execute_clears_on_failure(self):
        motion = MotionService(plan_success_rate=1.0, exec_success_rate=0.5)
        pose = Pose(position=[0.0, 0.0, 0.0], quat=[0.0, 0.0, 0.0, 1.0], frame_id="base", stamp=0.0)

        motion.plan(pose, "lane_A")
        self.assertIsNotNone(motion.current_traj)

        # Force execution failure to verify trajectory is cleared
        with patch("sorter_demo.motion.random.random", return_value=1.0):
            self.assertFalse(motion.execute())

        self.assertIsNone(motion.current_traj)


if __name__ == "__main__":
    unittest.main()

