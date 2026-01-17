import os
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class InjectorApp(App):
    def build(self):
        self.layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.title_label = Label(
            text="[color=ff0000]ULTRA HS INJECTOR[/color]\n[size=15]ANY BODY PART = HEADSHOT[/size]",
            markup=True, font_size='22sp', halign='center'
        )
        
        self.btn = Button(
            text="START INJECTION",
            size_hint=(1, 0.3),
            background_color=(0, 1, 0, 1),
            font_size='20sp'
        )
        self.btn.bind(on_press=self.start_hack)
        
        self.layout.add_widget(self.title_label)
        self.layout.add_widget(self.btn)
        return self.layout

    def start_hack(self, instance):
        # كود الحقن عبر الروت في المحاكي أو الناسخ
        pkg = "com.dts.freefireth"
        offset = "0x14D9A20"
        value = "\\x00\\x00\\x80\\x43"
        
        cmd = f"su -c 'PID=$(pidof {pkg}); BASE=$(grep \"libil2cpp.so\" /proc/$PID/maps | head -n 1 | cut -d \"-\" -f1); printf \"{value}\" | dd of=/proc/$PID/mem bs=1 seek=$((0x$BASE + {offset})) conv=notrunc 2>/dev/null'"
        
        exit_code = os.system(cmd)
        if exit_code == 0:
            self.title_label.text = "✅ INJECTED SUCCESSFULLY!\nGo back to Game"
        else:
            self.title_label.text = "❌ FAILED!\nCheck Root/MultiApp"

if __name__ == "__main__":
    InjectorApp().run()
