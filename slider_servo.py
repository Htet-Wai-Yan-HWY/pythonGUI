from tkinter import *
import rospy
from std_msgs.msg import UInt16

rospy.init_node('servo_gui')
h = rospy.Publisher("sh",UInt16,queue_size=1)
v = rospy.Publisher("sv",UInt16,queue_size=1)

def send(val):
    h.publish(int(val))
    v.publish(int(val))

master = Tk()
master.geometry("600x600")
master.title("Servo_control")
w1 = Scale(master, from_=0, to=180, command=send)
w1.set(0)
w1.pack()

w2 = Scale(master, from_=0, to=180, orient=HORIZONTAL, command=send)
w2.set(0)
w2.pack()

#Button(master, text="Send", command=send).pack()

master.mainloop()