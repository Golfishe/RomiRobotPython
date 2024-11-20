from commands2 import Command
from commands2 import Subsystem


class bigSubsystem(Subsystem):

    def __init__(self):
        """Creates a new ExampleSubsystem."""
        super().__init__()


    def exampleMethodCommand()->Command:
        pass

    def exampleCondition(self)->bool:
        pass

    def periodic(self):
        # This method will be called once per scheduler run
        pass

    def simulationPeriodic(self):
        # This method will be called once per scheduler run during simulation
        pass
    
    def letsGetThisThingDriving(self):
        