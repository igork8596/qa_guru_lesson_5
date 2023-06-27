import os
from selene import browser as b, have, be, command
from faker import Faker

fake = Faker()


def test_demoqa():
    b.open('/automation-practice-form')
    first_name, last_name = [i for i in fake.name().split()]
    b.element('#firstName').should(be.blank).type(first_name)
    b.element('#lastName').should(be.blank).type(last_name)
    user_email = fake.email()
    b.element('#userEmail').should(be.blank).type(user_email)
    b.element('label[for="gender-radio-1"]').click()
    b.element('#userNumber').should(be.blank).type('9878763524')
    b.element('#dateOfBirthInput').click()
    b.element('[class="react-datepicker__month-select"]').click()
    b.element('[value="4"]').click()
    b.element('[class="react-datepicker__year-select"]').click()
    b.element('[value="1996"]').click()
    b.element('[class="react-datepicker__day react-datepicker__day--008"]').click()
    b.element('#subjectsInput').should(be.blank).type('Math').press_enter()
    for i in range(3):
        b.element(f'label[for="hobbies-checkbox-{i + 1}"]').click()
    b.element('#uploadPicture').send_keys(os.path.abspath('picture/Cat.jpeg'))
    b.element('#currentAddress').should(be.blank).type('996 William Rapid, New Gregoryton, UT 78395')
    b.element('#state').perform(command.js.scroll_into_view)
    b.element('#state').click()
    b.element('#react-select-3-option-1').click()
    b.element('#city').click()
    b.element('#react-select-4-option-1').click()
    b.element('#submit').perform(command.js.click)

    b.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form'))
    b.element('.table-responsive tr:nth-child(1) td:nth-child(1)').should(have.exact_text('Student Name'))
    name = first_name + ' ' + last_name
    b.element('.table-responsive tr:nth-child(1) td:nth-child(2)').should(have.exact_text(name))
    b.element('.table-responsive tr:nth-child(2) td:nth-child(1)').should(have.exact_text('Student Email'))
    b.element('.table-responsive tr:nth-child(2) td:nth-child(2)').should(have.exact_text(user_email))
    b.element('.table-responsive tr:nth-child(3) td:nth-child(1)').should(have.exact_text('Gender'))
    b.element('.table-responsive tr:nth-child(3) td:nth-child(2)').should(have.exact_text('Male'))
    b.element('.table-responsive tr:nth-child(4) td:nth-child(1)').should(have.exact_text('Mobile'))
    b.element('.table-responsive tr:nth-child(4) td:nth-child(2)').should(have.exact_text('9878763524'))
    b.element('.table-responsive tr:nth-child(5) td:nth-child(1)').should(have.exact_text('Date of Birth'))
    b.element('.table-responsive tr:nth-child(5) td:nth-child(2)').should(have.exact_text('08 May,1996'))
    b.element('.table-responsive tr:nth-child(6) td:nth-child(1)').should(have.exact_text('Subjects'))
    b.element('.table-responsive tr:nth-child(6) td:nth-child(2)').should(have.exact_text('Maths'))
    b.element('.table-responsive tr:nth-child(7) td:nth-child(1)').should(have.exact_text('Hobbies'))
    b.element('.table-responsive tr:nth-child(7) td:nth-child(2)').should(have.exact_text('Sports, Reading, Music'))
    b.element('.table-responsive tr:nth-child(8) td:nth-child(1)').should(have.exact_text('Picture'))
    b.element('.table-responsive tr:nth-child(8) td:nth-child(2)').should(have.exact_text('Cat.jpeg'))
    b.element('.table-responsive tr:nth-child(9) td:nth-child(1)').should(have.exact_text('Address'))
    b.element('.table-responsive tr:nth-child(9) td:nth-child(2)').should(
        have.exact_text('996 William Rapid, New Gregoryton, UT 78395'))
    b.element('.table-responsive tr:nth-child(10) td:nth-child(1)').should(have.exact_text('State and City'))
    b.element('.table-responsive tr:nth-child(10) td:nth-child(2)').should(have.exact_text('Uttar Pradesh Lucknow'))
    b.element('#closeLargeModal').click()
