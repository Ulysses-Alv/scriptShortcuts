import schedule
import time
import holdMouseButton
import spamClick
import deactivate

def schedules(timeInCentiSecond, function, argsOfFunction, isActivated) : # 100 CentiSeconds = 1seg.  eg: 20cs = 0.2segs.
    if(isActivated) :
        schedule.every((timeInCentiSecond / 100)).seconds.do(function, argsOfFunction)
        
schedules(1, deactivate.desactivate, "m", True) #Should be always true, Otherwise you could not stop it.
schedules(0.1, spamClick.spamClick, "f", "x", True)
schedules(1, holdMouseButton.holdClick, "h", False)

while deactivate.activated:
    schedule.run_pending()
    time.sleep(0.1)