from CircleShape import CircleShape

def test_circles_overlap():
    circle1 = CircleShape(100, 100, 20)
    circle2 = CircleShape(110, 100, 20)
    assert circle1.collides_with(circle2) == True

def test_circles_do_not_overlap():
    circle1 = CircleShape(100, 100, 10)
    circle2 = CircleShape(200, 200, 10)
    assert circle1.collides_with(circle2) == False

def test_circles_touch():
    circle1 = CircleShape(100, 100, 10)
    circle2 = CircleShape(120, 100, 10)
    assert circle1.collides_with(circle2) == True