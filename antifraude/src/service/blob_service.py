import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
from utils.Config import Config

def upload_blob(file, file_name):
    try:     
        #config = Config()   
        blob_service_client = BlobServiceClient.from_connection_string(Config.CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)
        blob_client.upload_blob(file, overwrite=True)
        return blob_client.url
    except Exception as ex:
        st.error(f"Erro ao enviar o arquivo {file_name} para o Azure Blob Storage: {ex}")
        return None