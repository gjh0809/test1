from sorter_demo import (
    HandEye,
    GraspPlanner,
    MotionService,
    SorterPipeline,
    StateMachine,
    VisionService,
)


def build_pipeline() -> SorterPipeline:
    # Mock extrinsic: camera frame aligned with base at 0.1 m height offset.
    T_cam_base = [
        [1.0, 0.0, 0.0, 0.0],
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0, 1.0, 0.1],
        [0.0, 0.0, 0.0, 1.0],
    ]

    handeye = HandEye(T_cam_base)
    planner = GraspPlanner(handeye)
    vision = VisionService()
    motion = MotionService()
    sm = StateMachine()
    return SorterPipeline(vision=vision, planner=planner, motion=motion, sm=sm)


def main():
    import argparse
    import time

    parser = argparse.ArgumentParser(description="分拣/拆垛示例循环运行")
    parser.add_argument("--iterations", type=int, default=5, help="循环次数，<=0 表示无限循环")
    parser.add_argument("--sleep", type=float, default=0.2, help="两次循环的间隔秒")
    args = parser.parse_args()

    pipeline = build_pipeline()
    total = 0
    ok = 0

    def run_one():
        nonlocal total, ok
        total += 1
        success = pipeline.run_once()
        if success:
            ok += 1
        print(f"[{total}] 结果: {'成功' if success else '失败'}，事件: {pipeline.sm.last_event}，累计: {ok}/{total}")

    if args.iterations <= 0:
        try:
            while True:
                run_one()
                time.sleep(args.sleep)
        except KeyboardInterrupt:
            print(f"终止，累计成功 {ok}/{total}")
    else:
        for _ in range(args.iterations):
            run_one()
            time.sleep(args.sleep)
        print(f"完成 {args.iterations} 次，成功 {ok}/{total}")


if __name__ == "__main__":
    main()

