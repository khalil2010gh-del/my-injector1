from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
import os

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        self.lbl = Label(text="INJECTOR READY", font_size='25sp')
        btn = Button(text="ACTIVATE 100% HS", size_hint=(1, 0.4), background_color=(0, 1, 0, 1))
        btn.bind(on_press=self.inject)
        
        layout.add_widget(self.lbl)
        layout.add_widget(btn)
        return layout

    def inject(self, instance):
        # أمر الحقن للناسخ أو الروت
        pkg = "com.dts.freefireth"
        offset = "0x14D9A20"
        value = "\\x00\\x00\\x80\\x43"
        
        cmd = f"su -c 'PID=$(pidof {pkg}); BASE=$(grep \"libil2cpp.so\" /proc/$PID/maps | head -n 1 | cut -d \"-\" -f1); printf \"{value}\" | dd of=/proc/$PID/mem bs=1 seek=$((0x$BASE + {offset})) conv=notrunc 2>/dev/null'"
        
        os.system(cmd)
        self.lbl.text = "✅ SUCCESS!"

if __name__ == "__main__":
    MainApp().run()
