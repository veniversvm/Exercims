class SpaceAge:
    seconds = 0
    def __init__(self, seconds):
        self.seconds = seconds
        
    def _calculate_years(self, orbital_period):
        return round((((self.seconds / orbital_period / 60) / 60)/24) / 365.25, 2)
    def on_earth(self):
        return self._calculate_years(1.0)
    def on_mercury(self):
        return self._calculate_years(0.2408467) 
    def on_venus(self):
        return self._calculate_years(0.61519726) 
    def on_mars(self):
        return self._calculate_years(1.8808158)
    def on_jupiter(self):
        return self._calculate_years(11.862615)
    def on_saturn(self):
        return self._calculate_years(29.447498)
    def on_uranus(self):
        return self._calculate_years(84.016846)
    def on_neptune(self):
        return self._calculate_years(164.79132)
