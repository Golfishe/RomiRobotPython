import commands2
import wpilib.drive
from wpilib import PWMSparkMax
from wpilib.drive import DifferentialDrive

class MySubsystem(commands2.Subsystem):

    def __init__(self):
        super().__init__()

        self.controller = wpilib.Joystick(0)

        m_leftMotor = PWMSparkMax(0)
        m_rightMotor = PWMSparkMax(1)
        
        self.DifferentialDrive = DifferentialDrive(m_leftMotor, m_rightMotor)

        m_rightMotor.setInverted(True)
        

    def robotDrive(self, yspeed, zrotation):
        self.DifferentialDrive.arcadeDrive(yspeed, zrotation) # (-self.controller.getRawAxis(0), self.controller.getRawAxis(1))
        pass

    def teleopPeriodic(self):
        # This method will be called once per scheduler run
        # self.drive(self, -self.controller.getY(), -self.controller.getX())
        pass

    def simulationPeriodic(self):
        # This method will be called once per scheduler run during simulation
        pass

    