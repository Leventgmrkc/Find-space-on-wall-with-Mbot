# version1_without_probability
# codes make you happy

import event, time, cyberpi, mbuild, mbot2, random
import time

@event.start
def on_start():
    cyberpi.console.set_font(12)
    cyberpi.console.println("Press “B” to FİND SPACE XXX")
    cyberpi.console.println("Press “A” to restart")
    while not cyberpi.controller.is_press('b'):
      # DO SOMETHING
      pass
    initial_state = True
    a = 0 # counter for turning side
    while True:
        if initial_state :
            print("A equals to : ",a)
            print("\n basa gelduk ")
            mbot2.forward(30)
            time.sleep(1)


            if a == 0: # checking left wall first
                mbot2.turn_left(27)
                time.sleep(1)
                if mbuild.ultrasonic2.get(1) > 12: # if there is no wall in fronr of it check size
                    cyberpi.led.on(255, 255, 0)

                    diss1 = mbuild.ultrasonic2.get()
                    cyberpi.console.println("Reading diss 1 : %d" % diss1)
                    

                    mbot2.turn_right(10)
                    time.sleep(1)
                    diss2 = mbuild.ultrasonic2.get()
                    cyberpi.console.println("Reading diss 2 :%d" % diss1)

                    if diss1 and diss2 > 30:        # if size is enough get in wall
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
                    else : 
                        mbot2.turn_right(17)
                        time.sleep(1.2)
                        a=2
                        print("Checking left  : ",a)

                else: # there is no wall on left side next we should check right side
                    mbot2.turn_right(27)
                    time.sleep(1)
                    a=2
                    print("Checking left  : ",a)

            if a==2:    # checking right
                mbot2.turn_right(27)
                time.sleep(1)
                if mbuild.ultrasonic2.get(1) > 12:
                    cyberpi.led.on(255, 0, 0)
                    cyberpi.audio.play_music(120, 0.95)
                    mbot2.turn_left(30)
                    time.sleep(1.4)
                    mbot2.forward(19)
                    time.sleep(1)
                    mbot2.turn_right(27)
                    time.sleep(1)

                    mbot2.forward(60)
                    time.sleep(2)                                  
                    print("passing from wall")                
                    mbot2.turn_right(107)
                    time.sleep(3) 
                    initial_state = False
                    mbot2.EM_stop()
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