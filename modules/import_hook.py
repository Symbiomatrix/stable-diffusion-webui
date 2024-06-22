# this will break any attempt to import xformers which will prevent stability diffusion repo from trying to use it
import sys
from modules.shared import cmd_opts
if not cmd_opts.xformers:
    sys.modules["xformers"] = None

# Hack to fix a changed import in torchvision 0.17+, which otherwise breaks
# basicsr; see https://github.com/AUTOMATIC1111/stable-diffusion-webui/issues/13985
try:
    import torchvision.transforms.functional_tensor  # noqa: F401
except ImportError:
    try:
        import torchvision.transforms.functional as functional
        sys.modules["torchvision.transforms.functional_tensor"] = functional
    except ImportError:
        pass  # shrug...
