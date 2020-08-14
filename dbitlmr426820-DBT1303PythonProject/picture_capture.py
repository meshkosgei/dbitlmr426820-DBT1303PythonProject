  camera.capture('picam_img.jpg')
  print('snap!')
  with open("picam_img.jpg", "rb") as imageFile:
    str = base64.b64encode(imageFile.read())
    try:
      aio.send('picam', str)
    except:
      print('Sending camera image failed...')