import gradio as gr
import os
from preprocess import preprocess_image
from prompt_generator import generate_prompt_from_image
from controlnet_inference import generate_with_controlnet

TEMP_INPUT = "temp/input.png"
TEMP_OUTPUT = "temp/generated.png"

def sketch2image(sketch_img):
    sketch_img.save(TEMP_INPUT)

    # Step 1: Canny edge preprocessing
    edge_img = preprocess_image(TEMP_INPUT)

    # Step 2: Prompt generation using BLIP
    prompt = generate_prompt_from_image(TEMP_INPUT)

    # Step 3: Generate image using ControlNet + SD
    output_img = generate_with_controlnet(prompt, edge_img)
    output_img.save(TEMP_OUTPUT)

    return edge_img, prompt, output_img

with gr.Blocks(title="Sketch-to-Image AI Drawer") as demo:
    gr.Markdown("## 🎨 AI Drawer: Sketch to Image using ControlNet")
    gr.Markdown("Upload a sketch. A prompt will be generated and used to produce a detailed image.")

    with gr.Row():
        with gr.Column():
            input_image = gr.Image(type="pil", label="Upload Sketch")
            generate_btn = gr.Button("Generate Image")

        with gr.Column():
            edge_output = gr.Image(type="pil", label="Canny Edges")
            generated_prompt = gr.Textbox(label="Generated Prompt")
            output_image = gr.Image(type="pil", label="Final Output")
            download_btn = gr.File(label="Download Image")

    def on_generate(sketch_img):
        edge, prompt, final = sketch2image(sketch_img)
        final.save(TEMP_OUTPUT)
        return edge, prompt, final, TEMP_OUTPUT

    generate_btn.click(
        fn=on_generate,
        inputs=[input_image],
        outputs=[edge_output, generated_prompt, output_image, download_btn]
    )

demo.launch()
