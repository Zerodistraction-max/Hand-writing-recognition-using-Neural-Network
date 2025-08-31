import streamlit as st
from streamlit_drawable_canvas import st_canvas
import numpy as np
import tensorflow as tf
from tensorflow import keras
from PIL import Image
import base64
import io

# --- 1. Load the Model ---
@st.cache_resource
def load_model():
    """Loads the pre-trained Keras model and caches it."""
    try:
        model = keras.models.load_model("mnist_model.h5")
        return model
    except Exception as e:
        st.error(f"Error: Could not load the model. Please make sure 'mnist_model.h5' is in the same directory.")
        st.stop()

model = load_model()

# --- 2. Streamlit UI Components ---
st.set_page_config(
    page_title="Handwritten Digit Recognizer",
    page_icon="✍️",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("✍️ Handwritten Digit Recognizer")
st.markdown("Draw a single digit (0-9) in the canvas below.")

# Define a container for the app
with st.container(border=True):
    # Create a canvas component
    canvas_result = st_canvas(
        stroke_width=20,
        stroke_color="#2c3e50",
        background_color="#FFFFFF",
        height=280,
        width=280,
        drawing_mode="freedraw",
        key="canvas",
    )

    # Add a button to trigger the prediction
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🔮 Predict", use_container_width=True):
            if canvas_result.image_data is not None:
                # --- 3. Preprocess the Image ---
                # Convert the image data to a Pillow Image object
                img_data = canvas_result.image_data.astype(np.uint8)
                img = Image.fromarray(img_data).convert('L') # Convert to grayscale

                # Resize and normalize the image
                img = img.resize((28, 28))
                img_array = np.array(img).astype('float32')

                # Invert colors (black on white) and normalize to [0, 1]
                img_array = 255.0 - img_array
                img_array /= 255.0

                # Reshape for the model
                # The model expects a shape of (batch_size, 28, 28, 1)
                img_array = np.expand_dims(img_array, axis=0) # Add batch dimension
                img_array = np.expand_dims(img_array, axis=-1) # Add channel dimension

                # --- 4. Make a Prediction ---
                prediction = model.predict(img_array)
                predicted_class = np.argmax(prediction, axis=1)[0]
                confidence = np.max(prediction) * 100

                # --- 5. Display the Results ---
                st.success("✅ Prediction Complete!")
                st.markdown(
                    f"### Predicted Digit: <span style='color:#3498db; font-size: 2.5rem;'>{predicted_class}</span>",
                    unsafe_allow_html=True
                )
                st.markdown(
                    f"**Confidence:** <span style='color:#7f8c8d;'>{confidence:.2f}%</span>",
                    unsafe_allow_html=True
                )
            else:
                st.warning("Please draw a digit first.")
    with col2:
        if st.button("🧼 Clear Canvas", use_container_width=True):
            # This is the corrected line to clear the canvas state
            del st.session_state.canvas
            st.rerun()

st.markdown("---")
st.markdown("Created with TensorFlow, Streamlit, and `streamlit-drawable-canvas`.")
st.markdown("Made by Suryansh Sapehia")
