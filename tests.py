import unittest
from strava import get_avg_week_distance, get_stats_text, get_time

stats = {
    'biggest_ride_distance': 100344.0,
    'biggest_climb_elevation_gain': 655.0,
    'recent_ride_totals': {
        'count': 1,
        'distance': 5059.68994140625,
        'moving_time': 1114,
        'elapsed_time': 1114,
        'elevation_gain': 30.0,
        'achievement_count': 0
    },
    'all_ride_totals': {
        'count': 307,
        'distance': 2635764,
        'moving_time': 551012,
        'elapsed_time': 708194,
        'elevation_gain': 27238
    },
    'recent_run_totals': {
        'count': 8,
        'distance': 105784.31884765625,
        'moving_time': 37928,
        'elapsed_time': 38552,
        'elevation_gain': 2636.0,
        'achievement_count': 0
    },
    'all_run_totals': {
        'count': 691,
        'distance': 11156392,
        'moving_time': 4476655,
        'elapsed_time': 4792369,
        'elevation_gain': 299429
    },
    'recent_swim_totals': {
        'count': 0,
        'distance': 0.0,
        'moving_time': 0,
        'elapsed_time': 0,
        'elevation_gain': 0.0,
        'achievement_count': 0
    },
    'all_swim_totals': {
        'count': 49,
        'distance': 30728,
        'moving_time': 70280,
        'elapsed_time': 76753,
        'elevation_gain': 8
    },
    'ytd_ride_totals': {
        'count': 1,
        'distance': 5060,
        'moving_time': 1114,
        'elapsed_time': 1114,
        'elevation_gain': 30
    },
    'ytd_run_totals': {
        'count': 4,
        'distance': 66924,
        'moving_time': 24043,
        'elapsed_time': 24546,
        'elevation_gain': 1668
    },
    'ytd_swim_totals': {
        'count': 0,
        'distance': 0,
        'moving_time': 0,
        'elapsed_time': 0,
        'elevation_gain': 0
    }
}

class MessageTests(unittest.TestCase):
    def test_avg_distance(self):
        result = get_avg_week_distance(stats['recent_run_totals'])
        self.assertEqual(result, '🏃 26.45 km')

    def test_recent_text(self):
        result = get_stats_text(stats['recent_run_totals'])
        self.assertEqual(result, '🏃 105.78 km\n⛰ 2636 m\n🕒 642h 32m\n🖐 8 runs')

    def test_ytd_text(self):
        result = get_stats_text(stats['ytd_run_totals'])
        self.assertEqual(result, '🏃 66.92 km\n⛰ 1668 m\n🕒 409h 6m\n🖐 4 runs')

class TimeTests(unittest.TestCase):
    def test_minutes(self):
        result = get_time(59)
        self.assertEqual(result, '59m')

    def test_hour(self):
        result = get_time(60)
        self.assertEqual(result, '1h')

    def test_hours(self):
        result = get_time(250)
        self.assertEqual(result, '4h 10m')


unittest.main()
