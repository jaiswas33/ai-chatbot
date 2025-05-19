# ai-chatbot
This is my Free AI chat bot exploring LLMs  and get my hands dirty with integration

# For Your Google API Key use secrete manager
## enable apis
gcloud services enable secretmanager.googleapis.com

## store your key
echo -n "Your_api_key" | gcloud secrets create gemini-api-key --data-file=-

## grant access to your cloud Run 
gcloud secrets add-iam-policy-binding gemini-api-key --member="serviceAccount:PROJECT_NUMBER-compute@developer.gserviceaccount.com" --role="roles/secretmanager.secretAccessor"

## mount the secret as an environment variable
gcloud run deploy gemini-chatbot \
  --image gcr.io/YOUR_PROJECT_ID/gemini-chatbot \
  --region us-central1 \
  --set-secrets GOOGLE_API_KEY=gemini-api-key:latest \
  --allow-unauthenticated
