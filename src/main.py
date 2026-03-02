import numpy as np
import image_io
import parameters
import activation
import atrous
import post_processing

img = image_io.load("images/Shapes.png")
params = parameters.read_parameters("filters/sobel_vertical.json")

kernel = np.array(params["kernel"])
activations = {"relu": activation.relu, "identity": activation.identity}
activation_fn = activations[params["activation"]]

img_out = atrous.atrous(img, kernel, params["rate"], params["stride_h"], params["stride_w"], activation_fn)

if "sobel" in params["name"]:
    img_out = post_processing.absolute(img_out)
    img_out = post_processing.histogram_expansion(img_out)

image_io.save(img_out, "outputs/Shapes.png")