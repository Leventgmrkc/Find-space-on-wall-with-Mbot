# version2_with_probability
# codes make you happy

import event, time, cyberpi, mbuild, mbot2, random
import time

@event.start
def on_start():#menu
    cyberpi.console.set_font(12)
    cyberpi.console.println("Press “B” to FİND SPACE XXX")
    cyberpi.console.println("Press “A” to restart")
    while not cyberpi.controller.is_press('b'):
      # DO SOMETHING
      pass
    initial_state = True
    a = 0 #counter for turning side
    prob=0 # probability counter
    while True:
        if initial_state :
            print("A equals to: ",a)
            
            mbot2.forward(30)
            time.sleep(1)


            if a == 0:
                mbot2.turn_left(29)
                time.sleep(1)
                if mbuild.ultrasonic2.get(1) > 12:
                    cyberpi.led.on(255, 255, 0)

                    diss1 = mbuild.ultrasonic2.get()
                    cyberpi.console.println("Reading diss 1 : %d" % diss1)
                    

                    mbot2.turn_right(10)
                    time.sleep(1)
                    diss2 = mbuild.ultrasonic2.get()
                    cyberpi.console.println("Reading diss 2 :%d" % diss1)

                    if diss1 and diss2 > 30:
                        if prob == 1: # if this is the second time that we found space then get in wall
                            cyberpi.led.on(255, 0, 0)
                            cyberpi.audio.play_music(120, 3)

                            mbot2.forward(19)
                            time.sleep(1)
                            mbot2.turn_left(16)
                            time.sleep(1)

                            mbot2.forward(60)
                            time.sleep(2)                                 
                            print("passing from wall")                   
                            mbot2.turn_right(107)
                            time.sleep(3) 
                            initial_state = False 
                            mbot2.EM_stop()
                        else : # else increase the probability counter for next time
                            cyberpi.led.on(0, 0, 255)
                            prob = 1
                            a=2
                            mbot2.turn_right(17)
                            time.sleep(1.2)
                    else : 
                        mbot2.turn_right(17)
                        time.sleep(1.2)
                        a=2
                        print("Checking left  : ",a)

                else:
                    mbot2.turn_right(29)
                    time.sleep(1)
                    a=2
                    print("Checking left  : ",a)

            if a==2:
                mbot2.turn_right(27)
                time.sleep(1)
                if mbuild.ultrasonic2.get(1) > 12:
                    if prob == 1:
                        cyberpi.led.on(255, 0, 0)
                        cyberpi.audio.play_music(120, 0.95)
                        mbot2.turn_left(30)
                        time.sleep(1.4)
                        mbot2.forward(19)
                        time.sleep(1)
                        mbot2.turn_right(30)
                        time.sleep(1)

                        mbot2.forward(60)
                        time.sleep(2)                                  
                        print("passing from wall")                
                        mbot2.turn_right(107)
                        time.sleep(3) 
                        initial_state = False
                        mbot2.EM_stop()
                    else :
                        cyberpi.led.on(0, 0, 255)
                        prob = 1
                        mbot2.turn_left(27)
                        time.sleep(1)
                        a=0
                else:
                    mbot2.turn_left(27)
                    time.sleep(1)
                    a=0
                    print("Checking right : ",a)


                       
        else :
            mbot2.EM_stop()
            cyberpi.console.print("Obstacle passed")
            print("Obstacle passed")
            break
        
        

@event.is_press('a')
def is_btn_press():
    cyberpi.restart()