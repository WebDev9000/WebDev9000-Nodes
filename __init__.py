from .IgnoreBraces import IgnoreBraces
from .SettingsSwitch import SettingsSwitch

NODE_CLASS_MAPPINGS = {
    "IgnoreBraces": IgnoreBraces,
	"SettingsSwitch": SettingsSwitch,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "IgnoreBraces": "Ignore Braces",
	"SettingsSwitch": "Settings Switch",
}

__all__ = [NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS]