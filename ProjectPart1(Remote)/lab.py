


class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3


    def __init__(self):
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False
    def mute(self):
        if self.__status == True:
            self.__volcopy = self.__volume
            if self.__muted == False:
                self.__muted = True
                self.__volume = 0
            elif self.__muted == True:
                self.__muted = False



    def channel_up(self):
        if self.__status == True:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            elif self.__channel != Television.MAX_CHANNEL:
                self.__channel += 1
    def channel_down(self):
        if self.__status == True:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            elif self.__channel != Television.MIN_CHANNEL:
                self.__channel -= 1
    def volume_up(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__volcopy
            if self.__volume == Television.MAX_VOLUME:
                self.__volume = Television.MAX_VOLUME
            else:
                self.__volume += 1
        return self.__volume
    def volume_down(self):
        if self.__status == True:
            if self.__muted == True:
                self.__muted = False
                self.__volume = self.__volcopy
            if self.__volume == Television.MIN_VOLUME:
                self.__volume = Television.MIN_VOLUME
            else:
                self.__volume -= 1
        return self.__volume
    def __str__(self):
        return str(self.__volume)



