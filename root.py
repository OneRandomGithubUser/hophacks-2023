from taipy.gui import Gui, notify, navigate, Html
from slow import *

root_md = """
#Application
<|content|>
"""

home_md = """
<img src="images/hedgehog.jpeg" alt="Hedgehog image" style="width:40%;height:40%;margin: auto;"></img>
<br />
<|Start|button|on_action=to_profiles_page|>
"""


def to_profiles_page(state):
    navigate(state, to="profiles")


profiles_html = Html("""
   <button onclick="toEmily()" style="margin: auto; width: 40%; height: 30%;">
      <div style="width: 30%; float: left">
         <img src="images/grandma.jpg" alt="grandma profile" style="border-radius: 50%; width: 50%; height: 50%"></img>
      </div> 
      <div style="margin: auto; float: center; text-align: center">
         <p style="font-size: 25px">Emily</p>       
      </div>   
   </button>
"""
)

def toEmily():
   navigate(to="slow_step1")


slow_step1 = """
## Place pill1 in the tray
<|Start|button|on_action=on_button_action|>
<br />

<audio autoplay>
    <source src="audio/audio1.mp3" type="audio/mpeg"></source>
    Your browser does not support the audio element.
</audio> 
"""


def on_button_action(state):
    notify(state, "info", f"Button Pressed")
    navigate(state, to="page2")


content = None
page2_md = """
## Take a picture and upload Image
<|{content}|file_selector|extensions=.jpg|on_action=on_upload_action|>
<br />

<audio autoplay>
    <source src="audio/audio2.mp3" type="audio/mpeg"></source>
    Your browser does not support the audio element.
</audio> 
"""
# Display image: <br /><|{content}|image|>


def on_upload_action(state):
    navigate(state, to="page3")
    # TODO: image processing


page3_md = """
##Analysis
"""


# def on_change(state, var_name, var_value):
#     if var_name == "text" and var_value == "Reset":
#         state.text = ""
#         return

pages = {
    "/": root_md,
    "home": home_md,
    "profiles": profiles_html,
    "slow_step1": slow_step1,
    "page2": page2_md,
    "page3": page3_md,
}

Gui(pages=pages, css_file="globalcss.css").run(dark_mode=True, use_reloader=True)
# Gui(pages=pages).run(dark_mode=True, use_reloader=True, ngrok_token="2VTxgUns8s131oUDbPOR4LHAHhn_4E535RK8fBuffvdRyUHsb")
