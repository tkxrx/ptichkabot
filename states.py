from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.storage.memory import MemoryStorage


storage: MemoryStorage = MemoryStorage()


class FSMSFillStartForm(StatesGroup):
    fill_name = State()
    fill_group = State()
    fill_subgroup = State()


class FSMMakeAppointment(StatesGroup):
    choose_day = State()
    choose_time = State()


class FSMMakeAppointmentV2(StatesGroup):
    choose_appointment = State()