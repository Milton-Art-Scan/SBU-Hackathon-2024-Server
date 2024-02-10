from landingai.pipeline.frameset import Frame
from landingai.predict import Predictor
import os
from dotenv import load_dotenv
import tempfile

current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up two directories to find the .env file
dotenv_path = os.path.join(current_dir, '..', '..', '.env')
load_dotenv(dotenv_path=dotenv_path)

predictor = Predictor(  
    endpoint_id=os.getenv('LANDING_LENS_ENDPOINT_ID'),
    api_key=os.getenv('LANDING_LENS_API_KEY'),
)


def get_inference(image_path):
    """
    Get inference for the given image from LandingAI's Landing Lens.

    Args:
        image_path (str): The path to the image file.

    Returns:
        list: A list of predictions.
    """
    frame = Frame.from_image(image_path)

    # Get the temporary directory
    temp_dir = tempfile.gettempdir()  # Get the temporary directory
    image_path = os.path.join(temp_dir, "resized-image.png")

    frame.save_image(image_path)
    frame.run_predict(predictor=predictor)
    frame.overlay_predictions()
    predictionsList = frame.predictions
    return predictionsList
