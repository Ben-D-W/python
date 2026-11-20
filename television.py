class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MAX_CHANNEL

    def power(self):
        if self.status:
            self.status = False
        else:
            self.status = True

    def mute(self):
        if self.muted:
            self.muted = False
        else:
            self.muted = True

    def channel_up(self):
        self.channel += 1
        if self.channel > self.MAX_CHANNEL:
            self.channel = self.MIN_CHANNEL

    def channel_down(self):
        self.channel -= 1
        if self.channel < self.MIN_CHANNEL:
            self.channel = self.MAX_CHANNEL

    def volume_up(self):
        self.volume += 1
        if self.volume > self.MAX_VOLUME:
            self.volume = self.MAX_VOLUME
        if self.muted:
            self.muted = False

    def volume_down(self):
        self.volume -= 1
        if self.volume < self.MIN_VOLUME:
            self.volume = self.MIN_VOLUME
        if self.muted:
            self.muted = False

    def __str__(self):
        volume = self.volume
        if self.muted:
            volume = 0
        return f'Power = {self.status}, Channel = {self.channel}, Volume = {volume}'