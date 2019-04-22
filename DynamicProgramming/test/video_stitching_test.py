import DynamicProgramming.video_stitching as vs
import unittest


class Test_TestVideoStitching(unittest.TestCase):
    def test_video_stitching_small(self):
        clips = [[0, 2], [4, 6], [8, 10], [1, 9], [1, 5], [5, 9]]
        T = 10

        self.assertEquals(3, vs.minimum_num_clips(clips, T))
        self.assertEquals(3, vs.minimum_num_clips_dp(clips, T))

    def test_video_stitching_med(self):
        clips = [[0, 1], [6, 8], [0, 2], [5, 6], [0, 4], [0, 3],
                 [6, 7], [1, 3], [4, 7], [1, 4], [2, 5], [2, 6], [3, 4],
                 [4, 5], [5, 7], [6, 9]]

        T = 9

        self.assertEquals(3, vs.minimum_num_clips_dp(clips, T))

    def test_video_stitching_none(self):
        clips = [[0, 1], [1, 2]]
        T = 5

        self.assertEquals(-1, vs.minimum_num_clips(clips, T))
        self.assertEquals(-1, vs.minimum_num_clips_dp(clips, T))


if __name__ == "__main__":
    unittest.main()
