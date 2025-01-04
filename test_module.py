import unittest
from time_series_visualizer_2 import draw_line_plot, draw_bar_plot, draw_box_plot

class TestPlots(unittest.TestCase):
    
    def test_draw_line_plot(self):
        fig = draw_line_plot()
        self.assertEqual(fig.get_figwidth(), 15)
        self.assertEqual(fig.get_figheight(), 5)

    def test_draw_bar_plot(self):
        fig = draw_bar_plot()
        self.assertEqual(fig.get_figwidth(), 15)
        self.assertEqual(fig.get_figheight(), 5)

    def test_draw_box_plot(self):
        fig = draw_box_plot()
        self.assertEqual(fig.get_figwidth(), 16)
        self.assertEqual(fig.get_figheight(), 6)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

