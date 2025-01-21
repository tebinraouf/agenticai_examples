from smolagents import CodeAgent, HfApiModel, Tool
import gradio as gr

# Setup image generation tool 
image_generation_tool = Tool.from_space(
    "black-forest-labs/FLUX.1-schnell",
    name="image_generator", 
    description="Generate an image from a prompt"
)
agent = CodeAgent(tools=[image_generation_tool], model=HfApiModel())

def generate_image(prompt):
    try:
        # 1) First, ask the agent to improve the prompt.
        #    We'll do only the 'improve' part here.
        improved_prompt_result = agent.run(
            f"Improve this prompt: {prompt}",
            additional_args={
                'user_prompt': prompt,
                'output': 'improved_prompt'
                }
        )
        # Convert the result to string
        improved_prompt = str(improved_prompt_result).strip()
        
        # 2) Now, use the improved prompt to generate the image
        image_result = agent.run(
            f"Generate an image from this improved prompt: {improved_prompt}",
            additional_args={'user_prompt': improved_prompt}
        )
        generated_image = str(image_result)

        # Return the image along with the improved prompt
        return generated_image, improved_prompt

    except Exception as e:
        return None, f"Error: {str(e)}"


# Create Gradio interface
interface = gr.Interface(
    fn=generate_image,
    inputs=gr.Textbox(label="Enter your image prompt"),
    outputs=[
        gr.Image(label="Generated Image"),
        gr.Textbox(label="Improved Prompt Used")
    ],
    title="AI Image Generator",
    description="Enter a prompt to generate an image using FLUX.1-schnell model (the prompt will be improved automatically).",
    examples=[
        ["a cat wearing a cape"],
        ["cyberpunk city at night with neon lights"]
    ],
    allow_flagging="auto",
    flagging_options=["Good", "Bad", "Neutral"]
)

# Launch the interface
if __name__ == "__main__":
    interface.launch()
