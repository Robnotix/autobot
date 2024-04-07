from pymycobot.mycobot import MyCobot

cobot = MyCobot("COM13", 115200)

print(cobot.is_controller_connected())
cobot.set_color(255,0,0)
print(cobot.get_angles())

# cobot.send_angles([0,0,0,0,0,0], 100)
for i in range(1,7):
    cobot.set_servo_calibration(i)

while True:
    angle = input("joint, angle:")
    joint_id, angle = [int(x) for x in angle.split(', ')]
    # cobot.send_angle(joint_id, angle, 20)
