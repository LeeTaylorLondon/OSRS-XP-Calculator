# Author: Lee Taylor
import math


def calc_xp(L:int) -> int:
    """ Return xp difference between L and L-1 """
    return math.ceil(0.25 * math.floor((L-1) + (300 * 2 ** ((L-1)/7))))

# Calc. XP, time in hours and days, with approx. data and time from levels X to Y
# Where X,Y = user input

def lvl_to_lvl(start_lvl:int=1, end_lvl:int=99, lvl_name:str="", xphr:int=80000, hrsd:float=15.0):
    """ start_lvl: starting level to calculate from
          end_lvl: target level to acquire
          xphr: xp gained per hour
          hrsd: hours played per day
    """
    sum_xp = 0
    for lvl in range(start_lvl + 1, end_lvl + 1):
        sum_xp += calc_xp(lvl)
    hours = round(sum_xp / xphr, 1)
    days = round(hours/hrsd, 1)
    print(f"From level [{start_lvl}] to [{end_lvl}] [{lvl_name}] @ [{xphr}/Hr] for [{hrsd}Hrs/Day]\n\
Hours: [{hours}], days: [{days}], XP Remaining: [{sum_xp}]\n")
    return sum_xp, hours, days

def xp_to_lvl(start_xp:int=1, end_lvl:int=99, lvl_name:str="", xphr:int=80000, hrsd:float=15.0):
    """ start_xp: starting xp to calculate from
          end_lvl: target level to acquire
          xphr: xp gained per hour
          hrsd: hours played per day
    """
    needed_xp = 0
    for L in range(1, end_lvl+1):
        needed_xp += calc_xp(L)
    remaining_xp = needed_xp - start_xp
    hours = round(remaining_xp / xphr, 1)
    days = round(hours/hrsd, 1)
    print(f"From XP [{start_xp}] to [{end_lvl}] [{lvl_name}] @ [{xphr}/Hr] for [{hrsd}Hrs/Day]\n\
Hours: [{hours}], days: [{days}], XP Remaining: [{remaining_xp}]\n")
    return remaining_xp, hours, days


# lvl_to_lvl(85, 95, "ATK")
# xp_to_lvl(3362605, 88, "ATK", 75000)
# lvl_to_lvl(85, 97, "ATK", 75000)
# xp_to_lvl(3663605, 87, "ATK", 75000)
# xp_to_lvl(2165605, 90, "DEF", 73000)
# lvl_to_lvl(80, 95, "DEF")
# xp_to_lvl(5446859, 95, "ATK", 81000)
xp_to_lvl(2893275, 90, "DEF", 79_000, 15)
xp_to_lvl(2893275, 90, "DEF", 79_000, 8)
xp_to_lvl(2893275, 99, "DEF", 79_000, 15)
xp_to_lvl(2893275, 99, "DEF", 79_000, 8)
xp_to_lvl(10176639, 99, "HP", 26_400, 15)
xp_to_lvl(10176639, 99, "HP", 26_400, 8)
xp_to_lvl(7026618, 99, 'THIEVING', 220_000, 1.5)
# xp_to_lvl(5446859, 99, "ATK", 81000)

# lvl_to_lvl(85, 91, "Thieving", 195000, 3)
# xp_to_lvl(6438100, 95, "Thieving", 228000, 2)
lvl_to_lvl(95, 99, "Thieving", 250000, 2)


