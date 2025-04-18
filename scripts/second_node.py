#!/usr/bin/env python3
import time
from datetime import datetime

while True:
#получаем время
	current_time = datetime.now().strftime("%H:%M:%S")
	print(f"Время:{current_time}")
	time.sleep(5)
