from datetime import timedelta
class Clock:
    def __init__(self, hours:int = 0, minutes:int = 0, seconds:int = 0) -> None:
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def str_update(self, update:str) -> None:
        hour, minute, second = update.split(":")
        self.hours = int(hour.strip())
        self.minutes = int(minute.strip())
        self.seconds = int(second.strip())

    def add_clocks(self, new_clock):
        hours_in_seconds = (self.hours + new_clock.hours) * 3600
        minutes_in_seconds = (self.minutes + new_clock.minutes) * 60
        seconds_in_seconds = self.seconds + new_clock.seconds
        total_seconds = hours_in_seconds + minutes_in_seconds + seconds_in_seconds
        new_hours, new_minutes, new_seconds = list(map(int, str(timedelta(seconds=total_seconds)).split(":")))
        created_clock = Clock(new_hours, new_minutes, new_seconds)
        return created_clock

    def __str__(self):
        output = f"{self.hours} hours, {self.minutes} minutes and {self.seconds} seconds."
        return output