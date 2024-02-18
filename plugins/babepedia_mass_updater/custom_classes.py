PERFORMER_FRAGMENT = """
id
name
measurements
weight
height_cm
ethnicity
gender
"""
class DebugException(Exception):
    pass
class WarningException(Exception):
    pass
class ErrorException(Exception):
    pass

class StashPerformer:
    def __init__(self, resp) -> None:

        self.__dict__.update(resp)

        self.cupsize        = None
        self.band           = None
        self.waist          = None
        self.hips           = None

        self.bust           = None
        self.bust_band_diff = None
        self.breast_volume  = None

        self.bmi = 0

        self.tags_list = []

        self.parse_measurements()
        self.calculate_bmi()
        self.set_bmi_tag()

        self.set_breast_size()
        self.set_breast_cup()

        self.set_hip_size()

        self.set_butt_size()

        self.set_height_type()

        self.match_body_shapes()
        self.set_type_descriptor()
