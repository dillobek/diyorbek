from aiogram.dispatcher.filters.state import StatesGroup,State

class PersonalData(StatesGroup):
    sname = State()
    name = State()
    byear = State()
    course = State ()
    phone = State()

class lotin(StatesGroup):
    Lotin2krill = State()
    krill2lotin = State()


class UserState(StatesGroup):
    rname = State ()
    rphone = State ()
    user_have_experience = State ()