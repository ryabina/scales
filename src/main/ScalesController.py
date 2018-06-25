from main.Scales import ScalesModel


class ScalesController:
    scales_instance = ScalesModel()

    def measure_weight(self):
        return self.scales_instance.weight

