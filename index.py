import schedule
import time
import holdMouseButton
import spamClick
import deactivate

def schedules(timeInCentiSecond, function, argsOfFunction, isActivated) : # 100 CentiSeconds = 1seg.  eg: 20cs = 0.2segs.
    if(isActivated) :
        schedule.every((timeInCentiSecond / 100)).seconds.do(function, argsOfFunction)
        
schedules(1, deactivate.desactivar, "w", True)
schedules(20, spamClick.spamClick, "f", True)
schedules(1, holdMouseButton.holdClick, "h", True)

while deactivate.activated:
    schedule.run_pending()
    time.sleep(0.1)