# gcp-translation-demo

This code borrows heavily from https://github.com/GoogleCloudPlatform/python-docs-samples/blob/main/translate/samples/snippets/translate_v3beta1_translate_document.py

It runs on Python3+. Make sure to configure the request before running to match your environment and source document.

Example (in main-translate.py):
```
request_config = {
    'project_id': 'gcp-translation-demo',
    'location': 'us-central1',
    'source': 'What is Cloud Translation.pdf',
    'mime_type': 'application/pdf',
    'lang_code': 'fr',
    'output': 'What is Cloud Translation[fr].pdf'
}
```

To run, 

1. Enable the Translation API on your google cloud project
2. Create a python virtualenv by running `python -m venv <name of virtualenv>`
3. Switch to the virtualenv by running `source <name of virtualenv>/bin/activate`
4. Install the requirements by running `pip install -r requirements.txt`
5. Configure the request by editing the values in `request_config` in main-translate.py
6. Run the code: `python main-translate.py`


