import unittest

from sorter_demo import HandEye, GraspPlanner, MotionService, SorterPipeline, StateMachine, VisionService


def _identity_extrinsic():
    return [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 1.0],
    ]


class PipelineTests(unittest.TestCase):
    def test_pipeline_success(self):
        handeye = HandEye(_identity_extrinsic())
        planner = GraspPlanner(handeye)
        vision = VisionService()
        motion = MotionService(plan_success_rate=1.0, exec_success_rate=1.0)
        sm = StateMachine()

        pipeline = SorterPipeline(vision=vision, planner=planner, motion=motion, sm=sm)
        self.assertTrue(pipeline.run_once())
        self.assertEqual(sm.last_event, "success")

    def test_pipeline_plan_failure_recovery(self):
        handeye = HandEye(_identity_extrinsic())
        planner = GraspPlanner(handeye)
        vision = VisionService()
        motion = MotionService(plan_success_rate=0.0, exec_success_rate=1.0)
        sm = StateMachine()

        pipeline = SorterPipeline(vision=vision, planner=planner, motion=motion, sm=sm)
        self.assertFalse(pipeline.run_once())
        self.assertIn(sm.last_event, {"plan_fail", "no_success"})


if __name__ == "__main__":
    unittest.main()

