# productiveware

[![forthebadge](https://forthebadge.com/images/badges/works-on-my-machine.svg)](https://forthebadge.com)

encrypts your files in order for you to be productive. for xhacks

## boilerplate

all boilerplate code taken from [here](https://github.com/djizco/mern-boilerplate)

## Building the python app

You can manually build the application yourself if you wanted to:

```
git clone https://github.com/productiveware-xhacks/productiveware.git

cd productiveware/py-app

pip install -r requirements.txt

cxfreeze launch.py --target-dir dist --base-name Win32GUI --include-modules atexit --icon productiveware/widgets/res/productiveware.png
```
