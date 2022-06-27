
def test_robot_fix(robot_fix):
    output=robot_fix.cli.exec("dir")
    print(output)