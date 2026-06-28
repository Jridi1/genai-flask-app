from ibm_watsonx_ai import Credentials
from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames

import warnings
warnings.filterwarnings("ignore")

credentials = Credentials(
    url = "https://eu-de.ml.cloud.ibm.com",  
    api_key = "ECkcwYkzynTyIfHI7hSgxL-2-QyVDhMEVCLo3OMBEATk"
)

params = {
    GenTextParamsMetaNames.DECODING_METHOD: "greedy",
	GenTextParamsMetaNames.MAX_NEW_TOKENS: 100
}
model = ModelInference(
    model_id='mistralai/mistral-medium-2505',
    params=params,
    credentials=credentials,
    project_id= "06881b66-454b-4f5a-8376-026d644e23df"
)
text = """
<|begin_of_text|><|start_header_id|>system<|end_header_id|>
You are an expert assistant who provides concise and accurate answers.<|eot_id|>

<|start_header_id|>user<|end_header_id|>
What is the capital of Canada?<|eot_id|>

<|start_header_id|>assistant<|end_header_id|>
"""


print(model.generate(text)['results'][0]['generated_text'])
