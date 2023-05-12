# Copyright 2021 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os
from google.cloud import translate_v3beta1 as translate

def translate_document(request_config: object):

    client = translate.TranslationServiceClient()
    
    project_id = request_config["project_id"]
    location = request_config["location"]
    file_path = request_config["source"]
    mime_type = request_config["mime_type"]
    lang_code = request_config["lang_code"]
    output_path = request_config["output"]
    
    parent = f"projects/{project_id}/locations/{location}"

    # Supported file types: https://cloud.google.com/translate/docs/supported-formats
    with open(file_path, "rb") as document:
        document_content = document.read()

    document_input_config = {
        "content": document_content,
        "mime_type": mime_type,
    }

    # Supported language types: https://cloud.google.com/translate/docs/languages
    response = client.translate_document(
        request={
            "parent": parent,
            "target_language_code": lang_code,
            "document_input_config": document_input_config,
        }
    )

    # To output the translated document, uncomment the code below.
    f = open(output_path, 'wb')
    f.write(response.document_translation.byte_stream_outputs[0])
    f.close()

    # If not provided in the TranslationRequest, the translated file will only be returned through a byte-stream
    # and its output mime type will be the same as the input file's mime type
    print("Response: Detected Language Code - {}".format(response.document_translation.detected_language_code))

# [END translate_v3beta1_translate_document]

request_config = {
    'project_id': 'gcp-translation-demo',
    'location': 'us-central1',
    'source': 'What is Cloud Translation.pdf',
    'mime_type': 'application/pdf',
    'lang_code': 'fr',
    'output': 'What is Cloud Translation[fr].pdf'
}

translate_document(request_config)