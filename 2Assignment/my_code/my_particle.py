""" Semplice script che definisce alcune particelle
"""
import math

LIGHT_SPEED = 1

class particle:
    """ Class describing a particle
    """
    def __init__(self, mass, charge, name, momentum=0.1):
        """ Constructor of the class
        """
        self._mass = mass            # Mev units
        self._charge = charge        # in e- units
        self.name = name
        self.momentum = momentum    # in MeV/c units

    def print_info(self):
        """ Print the particle information in a nice formatted way
        """
        print(f'Particle {self.name}\n', f'- Mass = {self.mass} MeV/c^2\n', \
                f'- Charge: {self.charge} e\n', f'- Momentum = {self.momentum} MeV /c\n', \
                f'- Energy = {self.energy} MeV')

    @property
    def mass(self):
        return self._mass

    @property
    def charge(self):
        return self._charge

    @property
    def energy(self):
        return math.sqrt((self.momentum * LIGHT_SPEED)**2 \
                + (self.mass * LIGHT_SPEED**2)**2)

    @property
    def momentum(self):
        return self._momentum

    @property
    def beta(self):
        if not (self.energy > 0.):
            return 0.
        else:
            return LIGHT_SPEED * self.momentum/self.energy

    @momentum.setter
    def momentum(self, new_momentum):
        if new_momentum < 0:
            print('The momentum must be > 0!')
            print('The momentum wil be set = 0')
            self._momentum = 0
            return
        else:
            self._momentum = new_momentum

    @energy.setter
    def energy(self, new_energy):
        if new_energy < self.mass:
            print(f'The energy must be > mass: {self.mass} Mev!')
            return
        else:
            self.momentum = math.sqrt(new_energy**2 - (self.mass * LIGHT_SPEED)**2)\
                    /LIGHT_SPEED
    @beta.getter
    def beta(self, new_beta):
        if (new_beta < 0.) or (new_beta > 1.):
            print('beta must be in [0.,1.] range.')
            return
        if not ((new_beta < 1.) and (self.mass > 0.)):
            print('only massless particles can travel at speed of light')
            return
        self.momentum = new_beta * LIGTH_SPEED * self.mass \
                        /math.sqrt(1-new_beta**2)

class proton(particle):
    """ Class describing a proton.
    """
    NAME = 'Proton'
    mass = 938.272
    charge = +1.
    def __init__(self, momentum=0.):
        super().__init__(self.mass, self.charge, self.NAME, momentum)

class alpha(particle):
    """ Class describing an Alpha nucleum.
    """
    NAME = 'Alpha'
    mass = 3727.3
    charge = +4.
    def __init__(self, momentum=0.):
        super().__init__(self.mass, self.charge, self.NAME, momentum)


if __name__ == '__main__':
    proton1 = proton(1000)
    proton1.print_info()
