from tsheets.repository import Repository
from datetime import datetime
import tsheets.models as models


class ScheduleEvent(Repository):
    pass


ScheduleEvent.add_me_to_subcls()
ScheduleEvent.add_url("/schedule_events")
ScheduleEvent.add_model(models.ScheduleEvent)
ScheduleEvent.add_actions(['list', 'add', 'edit', 'delete'])
ScheduleEvent.filter("ids", [int])
ScheduleEvent.filter("user_ids", [int])
ScheduleEvent.filter("schedule_calendar_ids", [int])
ScheduleEvent.filter("jobcode_ids", [int])
ScheduleEvent.filter("start", datetime)
ScheduleEvent.filter("end", datetime)
ScheduleEvent.filter("draft", str)
ScheduleEvent.filter("modified_before", datetime)
ScheduleEvent.filter("modified_since", datetime)
ScheduleEvent.filter("per_page", int)
ScheduleEvent.filter("page", int)
