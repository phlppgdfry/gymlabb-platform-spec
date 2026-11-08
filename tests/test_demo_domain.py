import unittest
from demo import domain


class CoachingTests(unittest.TestCase):
    def test_workout_volume_and_weekly_limit(self):
        r = domain.seed()[0]
        p = dict(id=r["id"], action="workout", sets=3, reps=8, load=40)
        for _ in range(3):
            r = domain.execute([r], p)
        self.assertEqual(domain.present([r])[0]["volume"], 2880)
        self.assertEqual(r["inactive"], 0)
        with self.assertRaises(ValueError):
            domain.execute([r], p)

    def test_checkin_review_lifecycle(self):
        r = domain.seed()[1]
        p = dict(
            id=r["id"], action="checkin", sleep=7.5, energy=3, note="Fictional note"
        )
        r = domain.execute([r], p)
        self.assertEqual(domain.attention(r), "Review check-in")
        r = domain.execute([r], dict(id=r["id"], action="review"))
        self.assertTrue(r["reviewed"])
        r = domain.execute([r], p)
        self.assertFalse(r["reviewed"])

    def test_impossible_and_fractional_set_counts_are_rejected(self):
        r = domain.seed()[0]
        for sets in [0, 1.5, 11, True]:
            with self.assertRaises(ValueError):
                domain.execute(
                    [r], dict(id=r["id"], action="workout", sets=sets, reps=8, load=20)
                )
