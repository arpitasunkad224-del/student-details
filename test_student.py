from student import get_student_details


def test_student_name():
    student = get_student_details(
        "Arpita", "01FE25BCA274", "Jain College", "Hubli"
    )
    assert student["name"] == "Arpita"


def test_student_usn():
    student = get_student_details(
        "Arpita", "01FE25BCA274", "Jain College", "Hubli"
    )
    assert student["usn"] == "01FE25BCA274"


def test_college_name():
    student = get_student_details(
        "Arpita", "01FE25BCA274", "Jain College", "Hubli"
    )
    assert student["college"] == "Jain College"


def test_city():
    student = get_student_details(
        "Arpita", "01FE25BCA274", "Jain College", "Hubli"
    )
    assert student["city"] == "Hubli"