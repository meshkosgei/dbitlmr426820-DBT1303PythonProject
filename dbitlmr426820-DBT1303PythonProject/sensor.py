  # read/send door sensor
  if door_sensor.value:
    print('Door Open!')
    # change indicator block to red
    aio.send(door_feed.key, 3)
  else:
    print('Door Closed.')
    # reset indicator block to green
    aio.send(door_feed.key, 0)
  # read/send motion sensor
  if door_sensor.value:
    if not prev_pir_value:
      print('Motion detected!')
      is_pir_activated = True
      # change indicator block to red
      aio.send(motion_feed.key, 3)
  else:
    if prev_pir_value:
      print('Motion ended.')
      is_pir_activated = False
      # reset indicator block to green
      aio.send(motion_feed.key, 0)