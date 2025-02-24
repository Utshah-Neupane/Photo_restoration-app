# from dotenv import load_dotenv
# load_dotenv()
# import replicate

# model = replicate.models.get("tencentarc/gfpgan")
# version = model.versions.get("0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c")

# def predict_image(filename):
#     # https://replicate.com/tencentarc/gfpgan/versions/0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c#input
#     inputs = {
#         # Input 
#         'img': open(filename, "rb"),

#         # GFPGAN version. v1.3: better quality, v1.4: more details and better identity
#         'version': "v1.4",

#         # Rescaling factor
#         'scale': 2
#     }

#     # Call to the replicate model to get the output
#     output = model.predict(**inputs)
#     print(output)
#     return output






# from dotenv import load_dotenv
# load_dotenv()
# import replicate
# import requests

# # Load Replicate model and version
# model = replicate.models.get("tencentarc/gfpgan")
# version = model.versions.get("0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c")

# def predict_image(filename):
#     # https://replicate.com/tencentarc/gfpgan/versions/0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c#input
#     inputs = {
#         # Input 
#         'img': open(filename, "rb"),

#         # GFPGAN version. v1.3: better quality, v1.4: more details and better identity
#         'version': "v1.4",

#         # Rescaling factor
#         'scale': 2
#     }

#     # Call to the replicate model to get the output (which will be a URL)
#     output = version.predict(**inputs)

#     # Download the image from the URL provided in the output
#     response = requests.get(output)

#     # Save the downloaded image to a file
#     with open("output.png", "wb") as file:
#         file.write(response.content)

#     print("output.png written to disk")
#     return "output.png"





from dotenv import load_dotenv
load_dotenv()
import replicate

# Load the Replicate model and version
model = replicate.models.get("tencentarc/gfpgan")
version = model.versions.get("0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c")

def predict_image(filename):
    # https://replicate.com/tencentarc/gfpgan/versions/0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c#input
    inputs = {
        # Input image
        'img': open(filename, "rb"),

        # GFPGAN version: v1.4 for better identity and more details
        'version': "v1.4",

        # Rescaling factor
        'scale': 2
    }

    # Use replicate.run() to get the model's output
    output = replicate.run(
        "tencentarc/gfpgan:0fbacf7afc6c144e5be9767cff80f25aff23e52b0708f17e20f9879b2f21516c", 
        input=inputs
    )

    print(output)
    return output

