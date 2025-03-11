import gradio as gr
from app.model_list import models
from llm.agent import agent_predict

def predict(message, history, model_name):

    response = agent_predict(message, history, model_name)

    return response['output']['answer']

def cost_to_str(cost):
    return ('$' + '%6s' % str(cost)) if cost is not None else ' N/A '

def cost_to_template(cost_input, cost_output, cost_img):

    cost_input_str = cost_to_str(cost_input)
    cost_output_str = cost_to_str(cost_output)
    cost_img_str = cost_to_str(cost_img)

    template = '%s / M input tokens  ||  %s / M output tokens  ||  %s / K input imgs' % (
        cost_input_str, cost_output_str, cost_img_str
    )

    return template

def cost_fn(evt: gr.SelectData):

    global models

    model_name_input = evt.value
    cost_input, cost_output, cost_img = models[model_name_input]['cost']

    return cost_to_template(cost_input, cost_output, cost_img)


if __name__ == '__main__':

    # only show OpenRouter API models for now, since we are not using ollama
    model_choices = [(model_conf['display_name'], model_name) for model_name, model_conf in models.items() if not model_conf['local_model']]
    model_name_default = 'mistralai/mistral-small-24b-instruct-2501'

    with gr.Blocks(title='Chatbot', fill_height=True) as demo:

        with gr.Row():

            with gr.Column(scale=4, min_width=300):
                model_selector = gr.Dropdown(model_choices, label="Select Model", value=model_name_default, scale=0)

            with gr.Column(scale=5, min_width=300):
                cost_display = gr.Textbox(info='Cost of model', value=cost_to_template(*models[model_name_default]['cost']), show_label=False)

        model_selector.select(cost_fn, inputs=None, outputs=cost_display)
        gr.ChatInterface(
            predict,
            type="messages",
            additional_inputs=[model_selector],
        )

    # for simplicity, force the port to be 7860
    demo.launch(server_name='0.0.0.0', server_port=7860)
