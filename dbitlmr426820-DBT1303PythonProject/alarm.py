  # Alarm System 
  is_alarm = aio.receive(alarm_feed.key)
  if (is_alarm.value == "ON"):
    # sample the current hour
    cur_time = time.localtime()
    cur_hour = time.tm_hour
    if (cur_hour > ALARM_HOUR and is_pir_activated == True):
      alarm_trigger()