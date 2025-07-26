import os

from flask import Flask, send_file, render_template_string

app = Flask(__name__)

class FilterManager:
    def __init__(self):
        self.filters = {
            'sepia': 'sepia(100%)',
            'grayscale': 'grayscale(100%)',
            'contrast': 'contrast(150%)',
            'brightness': 'brightness(150%)',
            'blur': 'blur(5px)',
            'vintage': 'sepia(80%) hue-rotate(-20deg)',
            'warm': 'saturate(150%) hue-rotate(10deg)',
            'cold': 'saturate(140%) hue-rotate(-10deg)',
            'dreamy': 'sepia(50%) hue-rotate(10deg) contrast(110%)',
            'retro': 'grayscale(50%) contrast(120%)',
            'cinema': 'contrast(130%) sepia(30%)',
            'sunset': 'sepia(70%) contrast(120%) hue-rotate(-10deg)',
            'dramatic': 'contrast(140%) saturate(150%)',
            'none': 'none'
        }

    def add_filter(self, name, filter_text):
        self.filters[name] = filter_text

    def apply_filter(self, filter_name):
        if filter_name in self.filters:
            return self.filters[filter_name]
        else:
            return 'none'

class EffectManager:
    def __init__(self):
        self.effects = {}
        self.current_effects = []

    def add_effect(self, name, effect_html):
        self.effects[name] = effect_html

    def apply_effect(self, name):
        if name in self.effects and name not in self.current_effects:
            self.current_effects.append(name)
        elif name in self.current_effects:
          self.current_effects.remove(name)

        return self.get_effects_html()

    def get_effects_html(self):
      effects_html = ''
      for name in self.current_effects:
        effects_html += self.effects[name]
      return effects_html

filter_manager = FilterManager()
effect_manager = EffectManager()

@app.route("/")
def index():
    with open('index.html', 'r') as f:
      template = f.read()
    
    effect_manager.add_effect('snow','<div id="snow"></div>')
    effect_manager.add_effect('rain', '<div id="rain"></div>')
    
    
    return render_template_string(template, snow=effect_manager.apply_effect('snow'), rain=effect_manager.apply_effect('rain'))


def main():
    port = int(os.environ.get('PORT', 80))
    print(f"Running on port: {port}")
    app.run(host='0.0.0.0', port=port, debug=True)


if __name__ == "__main__":
    main()



