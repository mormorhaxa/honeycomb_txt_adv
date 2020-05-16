class Lifewheel:
    """Base class for all game entities, created with 3 arguments:
        name as string
        max_source as int (<= 54)
        scale as int (default character scale == 3)
    """
    def __init__(self, name=None, max_source=None, scale=None):
        self.name = name
        self.max_source = max_source
        self.scale = scale
        
        self.current_source = self.max_source
        self.description = {}
        self.potencies = {
            "life": 0,
            "earth": 0,
            "water": 0,
            "energy": 0,
            "air": 0,
            "fire": 0
        }
        self.capacities = {
            "mastery": 0,
            "persistence": 0,
            "design": 0,
            "poise": 0,
            "sleight": 0,
            "charm": 0
        }

    def __str__(self):
        return f"Name: {self.name}" \
               f"\nMax Source: {self.max_source}" \
               f"\nScale: {self.scale}"

    def increase_max_source(self, source_increase):
        """Increases max_source up to 54
        Also increases current_source
        Receives int
        """
        if self.max_source + source_increase <= 54:
            self.max_source += source_increase
            if self.current_source + source_increase <= self.max_source:
                self.current_source += source_increase    

    def _increase_capacities(self):
        """Increases capacities, should never be called externally
        """
        pass

    def increase_potencies(self, element, potency_increase):
        """Increase potencies, receives str, int.
        """
        if sum(self.potencies.values()) + potency_increase \
        <= self.max_source // 3:
            if self.potencies[element] + potency_increase <= 3:
                self.potencies[element] += potency_increase
        self._increase_capacities()
    
    
    def set_description(self):
        """Ufda, still working out how to build modular descriptions
        """
        pass
    
