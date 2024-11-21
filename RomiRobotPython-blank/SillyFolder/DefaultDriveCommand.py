import typing
import commands2
import wpilib
from SillyFolder.MySubsystem import MySubsystem


class DefaultDriveCommand(commands2.Command):
    def __init__(
        self,
        drive: MySubsystem,
        forward: typing.Callable[[], float],
        rotation: typing.Callable[[], float],
    ) -> None:
        
        super().__init__()

        self.controller = wpilib.Joystick(0)

        self.drive = drive
        self.forward = forward
        self.rotation = rotation
        
        self.addRequirements(self.drive)


    def execute(self) -> None:
        self.drive.robotDrive(self.forward(), self.rotation())