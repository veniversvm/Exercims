class SpaceAge:
    seconds = 0
    def __init__(self, seconds):
        self.seconds = seconds

    def on_earth(self):
        return round((((self.seconds / 1.0 / 60) / 60)/24) / 365.25, 2)
    def on_mercury(self):
        return round(((( self.seconds / 0.2408467 / 60) / 60)/24) / 365.25, 2)
    def on_venus(self):
        return round((((self.seconds / 0.61519726 / 60) / 60)/24) / 365.25, 2) 
    def on_mars(self):
        return round((((self.seconds / 1.8808158 / 60) / 60)/24) / 365.25, 2)   
    def on_jupiter(self):
        return round((((self.seconds / 11.862615 / 60) / 60)/24) / 365.25, 2)  
    def on_saturn(self):
        return round((((self.seconds / 29.447498 / 60) / 60)/24) / 365.25, 2)  
    def on_uranus(self):
        return round((((self.seconds / 84.016846 / 60) / 60)/24) / 365.25, 2)   
    def on_neptune(self):
        return round(((( self.seconds / 164.79132 / 60) / 60)/24) / 365.25, 2) 