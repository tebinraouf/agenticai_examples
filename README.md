---
title: Prompt Craft
emoji: 😍
colorFrom: red
colorTo: yellow
sdk: gradio
sdk_version: "5.12.0"
app_file: app.py
pinned: false
---

# Prompt Craft

## Overview

This project leverages HuggingFace's `smolagent` library to create AI-generated images through a streamlined workflow.

## Technology Stack

- **Agent Framework**: Uses HuggingFace's `smolagent` with `Tool.from_space` implementation
- **Image Generation**: Powered by the `FLUX.1-schnell` model
- **Prompt Enhancement**: Utilizes `Qwen/Qwen2.5-Coder-32B-Instruct` model via HuggingFace Inference API

## How It Works

1. User provides an initial image prompt
2. The Qwen model enhances the prompt for better results
3. FLUX.1-schnell generates the final image based on the improved prompt

## Links

- [HuggingFace Smolagent Documentation](https://huggingface.co/docs/smolagents/main/en/index)
- [Qwen 2.5 Model](https://huggingface.co/Qwen/Qwen2.5-Coder-32B-Instruct)

## Prerequisites

- Python 3.x
- pip

## Setup

1. Clone the repository:

   ```sh
   git clone https://github.com/tebinraouf/agenticai_examples.git
   cd agenticai_examples
   ```

2. Create a virtual environment:

   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Create a `.env` file in the root directory of the project and add your environment variables:

   ```sh
   touch .env
   ```

   Example `.env` file:

   ```
   HF_TOKEN=your_api_key_here
   ```

4. Install the dependencies:

   ```sh
   pip install -r requirements.txt
   ```

5. Run the project:
   ```sh
   python app.py
   ```

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
