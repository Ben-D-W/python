class Television:
    """
    A class to represent a television
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Method to set default values of a television
        """
        self.status: bool = False
        self.muted: bool = False
        self.volume: int = self.MIN_VOLUME
        self.channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to turn the tv on and off
        """
        if self.status:
            self.status = False
        else:
            self.status = True

    def mute(self) -> None:
        """
        Method to mute and unmute the tv if it's on
        """
        if self.status:
            if self.muted:
                self.muted = False
            else:
                self.muted = True

    def channel_up(self) -> None:
        """
        Method to increase the channel number if the tv is on,
        wrapping around to the minimum channel if it goes past the maximum channel
        """
        if self.status:
            self.channel += 1
            if self.channel > self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Method to decrease the channel number if the tv is on,
        wrapping around to the maximum channel if it goes past the minimum channel
        """
        if self.status:
            self.channel -= 1
            if self.channel < self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Method to increase the volume number if the tv is on,
        setting the volume to the maximum if trying to increase past the maximum volume
        """
        if self.status:
            self.volume += 1
            if self.volume > self.MAX_VOLUME:
                self.volume = self.MAX_VOLUME
            if self.muted:
                self.muted = False

    def volume_down(self) -> None:
        """
        Method to decrease the volume number if the tv is on,
        setting the volume to the minimum if trying to decrease past the minimum volume
        """
        if self.status:
            self.volume -= 1
            if self.volume < self.MIN_VOLUME:
                self.volume = self.MIN_VOLUME
            if self.muted:
                self.muted = False

    def __str__(self) -> str:
        """
        Method to return a string representation of the television
        :return: Power Status, Channel, Volume
        """
        volume = self.volume
        if self.muted:
            volume = 0
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {volume}'