import threading
import os
from sklearn.ensemble import RandomForestClassifier

class Predictor:
    def __init__(self):
        self.model = RandomForestClassifier()
        self.running = False
        self.timer = None

    def get_status(self):
        return "✅ Running" if self.running else "⛔ Stopped"

    def predict_once(self, bot):
        prediction = "❤️ RED | Number: 5 | Big"
        bot.send_message(chat_id=os.getenv("ADMIN_CHAT_ID"), text=f"🎯 Prediction: {prediction}")
        if self.running:
            self.schedule_next(bot)

    def schedule_next(self, bot):
        self.timer = threading.Timer(60, self.predict_once, args=[bot])
        self.timer.start()

    def start(self, bot):
        self.running = True
        self.schedule_next(bot)

    def stop(self):
        self.running = False
        if self.timer:
            self.timer.cancel()
