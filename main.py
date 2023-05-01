import eel
# import rfcontroller
import json

# controller = rfcontroller.RFController() 

@eel.expose
def togglePlug(command):
    print(command)
    # controller.sendcode(command)

@eel.expose
def storeConfig(setting, value):
    config = {}
    with open('config.json', 'r') as openfile:
        config  = json.load(openfile)
    with open('config.json', 'w') as writefile:
        config[setting] = value
        json.dump(config, writefile)

@eel.expose
def loadConfig():
    with open('config.json', 'r') as openfile:
        config = json.load(openfile)
        eel.loadConfig(config)


if __name__ == "__main__":
    eel.init('web', allowed_extensions=[".js",".html"])
    # eel.start('index.html', cmdline_args=['--start-fullscreen'])
    eel.start('index.html', size=(600, 800))
