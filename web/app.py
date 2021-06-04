import streamlit as st
import warnings
warnings.filterwarnings('ignore')
import ipywidgets as widgets
from IPython.display import display, clear_output
####### please don't delete below line ########
# Author github/developeranaz
####### Please don't delete above line ########
# support me star my repo
# Image Widget
file = open("Aria2Rclone.jpg", "rb")
image = file.read()
image_headline = widgets.Image(
                    value=image,
                    format='jpg',
                    width='400'
                )
label_headline = widgets.Label(
                    #value='Aria2Mega',
                    #style={'description_width': 'large'}
                )
vbox_headline = widgets.VBox([label_headline])
# magnet/url
toruri = widgets.Text(placeholder='http://ser.ver.mp4' ,flex_flow='column' ,align_items='center')
magnetdl = widget.Text(placeholder='magnet:?xt=ur../announce' ,flex_flow='column' ,align_items='center')
# config
#config = widgets.Text(
#    value='',
#    placeholder='https://gist../rclone.conf',
#    description='Conf File Url',
#    disabled=False
#)

cloudname = widgets.Dropdown(
    options=['selectone',
'1sundaran1', 
'2sundaran2', 
'3sundaran3', 
'4sundaran4', 
'Fauthor', 
'JinjaMega', 
'Pingme998', 
'sundaranmega' 
            ],
    value='selectone',
    description='cloudname:',
    disabled=False,
)

# CLOUDNAME
#cloudname = widgets.Text(
          # headline='kokk',
          # value='',
   #        placeholder='MyDrive1',
    #       description='Cloudname:',
    #       disabled=False
    #    )
cloudname.headline = 'k3yfhh'
# number of threads
threats = widgets.IntSlider(
            value=10, # default value
            min=2, 
            max=12,
            step=1,
           # style='danger'
            style={'description_width': 'initial', 'handle_color': '#f84834'} 
        )

# button down and up
from ipywidgets import Button
button_send= Button(description='START UPLOAD',button_style='danger' ,border='solid',width='50%',tooltip='Send')
button_send.layout.align_items = 'center'
output = widgets.Output()
def on_button_clicked(event):
    with output:
        clear_output()
        #rclone version
        %mkdir /home/{cloudname.value}
        %cd /home/{cloudname.value}
        #%rm *
        clear_output()
        #! wget -nc {config.value} -O '/.config/rclone/rclone.conf'
        ! rclone copy /Essential-Files/d {cloudname.value}:
        clear_output()
        ! aria2c -x{threats.value} '{toruri.value}'
        ! /Essential-files/t-get/app.js '{magnetdl.value}'
        ! rclone copy --progress --stats-one-line /home/{cloudname.value} {cloudname.value}:
        print(f"Your file uploaded to {cloudname.value} at {threats.value} x threads")
button_send.on_click(on_button_clicked)
vbox_result = widgets.VBox([button_send, output])

import ipywidgets as widgets
#text00 = widgets.HTML('Trouble Uploading ?')
#link00 = widgets.HTML(
   # value="<fofontnt color='lime'><center><h6><a href=https://github.com/developeranaz/Aria2-Rclone-Remote-Uploader-HEROKU target='_blank'>Issues can be reported here </a>",
#)

link01 = widgets.HTML(
    value="<font color='lime'><center><h6>DONATE BTC: 1J48LksQNiASuj48nwYATXdFzQSwdrnx7c <br><a href=https://github.com/developeranaz target='_blank'>DEVELOPERANAZ </a> <br><a href=https://github.com/developeranaz/Aria2-Rclone-Remote-Uploader-HEROKU target='_blank'>Trouble Uploading ? Readme </a><br><a href=https://github.com/developeranaz/Aria2-Rclone-Remote-Uploader-HEROKU/issues target='_blank'>Issues can be reported here </a>",
)


# texts+html+mark...
#text_0 = widgets.HTML(value="<center><h1><u>Aria2Mega</u></h1></center>")
text_1 = widgets.HTML(value="<h4>Thread or Max connection Per download</h4>")
line1 = widgets.HTML(value="<hr>")
#btc= widgets.HTML(value="<font color='lime'><center><h6>DONATE BTC: 1J48LksQNiASuj48nwYATXdFzQSwdrnx7c <br> Developed by developeranaz </h6></center></font>")
#text_2= widgets.HTML(value="<h4>Paste your config file in url,use git gist  </h4>")
#text_3= widgets.HTML(value="<h4>Type your Mega Password here</h4>")
text_4= widgets.HTML(value="<h4>Paste Direct URL link here</h4>")
text_magnet= widgets.HTML(value="<h4>Paste magnet/.torrent links here</h4>")
text_5= widgets.HTML(value="<h4>Select your Remote</h4>")
vbox_text = widgets.VBox([image_headline, line1, text_4, toruri, magnetdl, line1, text_1, threats, line1, text_5, cloudname, line1,line1, vbox_result, link01])
page = widgets.HBox([vbox_headline, vbox_text])
display(page)
