This is an **Azure Container App** which does **Paddy Disease Classification** using **Streamlit** as the UI and Azure Custom Vision API               

Also refer the article [Paddy Disease Classification using Azure AI](https://dev.to/ambarishg/paddy-doctor-paddy-disease-classification-1b7i) for the details of building the Computer Vision Model         

## Update -  KeyVault and Secrets support with System Assigned Identity added     

1. Create a KeyVault in Azure    
2. Add all the secrets in the KeyVault [ **key-vault-secrets.png** ]        
3. Add System Assigned Identity flag on in the Container App. Refer the image **paddy-system-assigned-identity.png** on how this is done     
4. The **paddyui_identity** has the implementation details of the code for System Assigned Identity 

The KeyVault URL is being stored as **secured environment variable**     



