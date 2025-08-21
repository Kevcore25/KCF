from KCFSyntax import *

def load():
    # Remove command feedback
    run('gamerule sendCommandFeedback false')
    run('gamerule doDaylightCycle false')


def rain():
    currenttick = 599
    run('weather rain 1d')

def thunder():
    currenttick = 599
    run('weather thunder 1d')

def done():
    started = 0
    run('weather clear 1d')
    print("Done!")

def start():
    # Starts the time thing
    print("Starting in 30 seconds...")

    # Start locking the player movement
    kill('@e[type=marker,tag=tw.lock]')
    summon(marker, '~ ~ ~', {"Tags": '[tw.lock]'})
    run('execute at @s as @n[type=marker,tag=tw.lock] run tp @s ~ ~ ~ ~ ~')
    started = 1
    currenttick = 0

    # Clear weather just in case
    run('weather clear 1d')

    # Schedule at the end of each day to change weather
    schedule('5400t', rain)
    schedule('10200t', thunder)
    schedule('15000t', done)

def tick():
    if started == 1:
        currenttick += 1

        # Early sunrise ? 
        if currenttick == 600:  run('time set 23500')
        # Sunrise
        if currenttick == 1200: run('time set 0')
        # Morning
        if currenttick == 1800: run('time set 3000')
        # Noon
        if currenttick == 2400: run('time set 6000')
        # Afternoon
        if currenttick == 3000: run('time set 9000')
        # Sunset
        if currenttick == 3600: run('time set 12000')
        # Night
        if currenttick == 4200: run('time set 13500')
        # Midnight
        if currenttick == 4800: run('time set 16000')

        # Lock player
        run('tp @a @n[type=marker,tag=tw.lock]')