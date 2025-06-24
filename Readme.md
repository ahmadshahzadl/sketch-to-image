# 🖌️ AI Drawer: Sketch-to-Image Generator

This project is an AI-powered **Sketch-to-Image Generator** that allows users to upload a sketch (hand-drawn or digital), automatically detects its edges using **Canny Edge Detection**, generates a **text prompt using BLIP** (a vision-language model), and finally uses **ControlNet + Stable Diffusion** to create a high-quality, photorealistic image.

---

## ✨ Key Features

* 🖼️ Upload any sketch or outline drawing
* 🔍 Applies **Canny edge detection** to extract key structure
* 🧠 Uses **BLIP** to automatically generate a text prompt from the image
* 🎨 Feeds the edges and prompt into **ControlNet + Stable Diffusion** to generate a realistic image
* 🧑‍💻 Easy-to-use **Gradio web interface**
* 📀 Option to download the final image

---

## 📦 Dependencies

Install all required packages using:

```bash
pip install -r requirements.txt
```

### `requirements.txt` Includes:

* `torch` – Deep learning engine (PyTorch)
* `diffusers` – HuggingFace library for image generation
* `transformers` – To load BLIP for prompt generation
* `opencv-python` – For Canny edge detection
* `Pillow` – Image processing
* `gradio` – Web UI
* `accelerate` – Device management
* `xformers` – (optional) Speed-up for GPU inference

---

## 💻 System Requirements

| Component | Requirement             |
| --------- | ----------------------- |
| OS        | Windows / macOS / Linux |
| Python    | 3.9 or later            |
| GPU       | NVIDIA GPU with CUDA    |
| RAM       | 8 GB minimum            |

🟡 **No GPU?** Use Google Colab (see below).

---

## 🚀 How to Run Locally

1. **Clone the repo** or create the folder manually
2. Install Python 3.9+
3. (Optional) Create virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate  # On Windows
   ```
4. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
5. Create a folder named `temp/` in the project root:

   ```bash
   mkdir temp
   ```
6. Run the app:

   ```bash
   python app.py
   ```
7. A browser window will open at:

   ```
   http://127.0.0.1:7860/
   ```

---

## 🧪 Example Workflow

1. Upload a sketch or drawing
2. The app shows:

   * The Canny edge map
   * The AI-generated text prompt
   * The final image based on your sketch + prompt
3. Click “Download” to save the result

---

## 📁 Project Structure

```
sketch2image/
├── app.py                  # Gradio app interface
├── preprocess.py           # Canny edge detection
├── prompt_generator.py     # BLIP caption generation
├── controlnet_inference.py # Stable Diffusion + ControlNet
├── requirements.txt        # Dependencies
├── temp/                   # Temp file storage
└── README.md               # Project info
```

---

## ☁️ Google Colab Version

Don't have a GPU? Run the full project in the cloud using Google Colab (free GPUs).

> 🔗 [Colab Notebook (coming soon)]()

---

## 🤝 Acknowledgements

* [HuggingFace Transformers](https://huggingface.co/docs/transformers/index)
* [BLIP: Bootstrapped Language Image Pretraining](https://huggingface.co/Salesforce/blip-image-captioning-base)
* [ControlNet](https://github.com/lllyasviel/ControlNet)
* [Stable Diffusion v1.5](https://huggingface.co/runwayml/stable-diffusion-v1-5)
* [Gradio](https://www.gradio.app/)

---

## 📜 License

This project is for **educational and research purposes** only. Always respect the licenses and usage terms of the models and libraries used.
