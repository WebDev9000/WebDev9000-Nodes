class SettingsSwitch:
    def __init__(self, ):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "preset": (["low noise", "high noise"],),
            }
        }

    RETURN_TYPES = ("INT","FLOAT")
    RETURN_NAMES = ("steps","denoise")
    OUTPUT_NODE = True
    FUNCTION = "doit"
    CATEGORY = "WebDev9000"

    def doit(self, preset):

        if (preset == "low noise"):
            steps = 5
            denoise = 0.35
        else:
            steps = 10
            denoise = 0.5

        return (steps, denoise)