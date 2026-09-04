import usb_hid
import storage
import supervisor

# Give your macropad a custom USB device name
supervisor.set_usb_device_name("XIAO 3x3 Macropad")

# Enable standard keyboard and media control functions over USB
usb_hid.enable((
    usb_hid.Device.KEYBOARD,
    usb_hid.Device.CONSUMER_CONTROL  # Crucial for your volume/media keys!
))

# Optimize storage behavior
storage.remount("/", readonly=False)
