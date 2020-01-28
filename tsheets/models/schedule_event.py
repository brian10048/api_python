from tsheets.model import Model
from datetime import datetime


class ScheduleEvent(Model):
    pass


ScheduleEvent.add_field("id", int)
ScheduleEvent.add_field("schedule_calendar_id", int)
ScheduleEvent.add_field("start", datetime)
ScheduleEvent.add_field("end", datetime)
ScheduleEvent.add_field("all_day", bool)
ScheduleEvent.add_field("assigned_user_ids", [int])
ScheduleEvent.add_field("jobcode_id", int)
ScheduleEvent.add_field("active", bool)
ScheduleEvent.add_field("draft", bool)
ScheduleEvent.add_field("timezone", str)
ScheduleEvent.add_field("title", str)
ScheduleEvent.add_field("notes", str)
ScheduleEvent.add_field("location", str)
ScheduleEvent.add_field("color", str)
ScheduleEvent.add_field("last_modified", datetime)
ScheduleEvent.add_field("created", datetime)
