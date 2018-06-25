import unittest
from main.ScalesController import ScalesController
from unittest import mock
import main.Scales


class ScalesControllerTest(unittest.TestCase):

    def test_measure_mass(self):
        # Arrange
        expected_weight = 15000
        scales_controller = ScalesController()
        with mock.patch('main.Scales.ScalesModel.weight',  new_callable=mock.PropertyMock) as mock_scales_model_weight:
            mock_scales_model_weight.return_value = expected_weight
            scales_model = main.Scales.ScalesModel()
            print(scales_model.weight)
        # Act
            actual_weight = scales_controller.measure_weight()
        # Assert
            self.assertEqual(expected_weight, actual_weight)

