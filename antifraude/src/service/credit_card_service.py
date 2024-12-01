from azure.core.credentials import AzureKeyCredential
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest
from utils.Config import Config

def analize_credit_card(blob_url):
    try:
        credential = AzureKeyCredential(Config.KEY)

        document_client = DocumentIntelligenceClient(endpoint=Config.ENDPOINT, credential=credential)

        card_info = document_client.begin_analyze_document(
            "prebuilt-creditCard", url_source=blob_url)
        result = card_info.result()
        
        for document in result.documents:
            fields = document.get("fields", {})
            return {
                "card_name": fields.get('CardholderName', {}).get('content'),
                "card_number": fields.get("CardNumber", {}).get('content'),
                "expiration_date": fields.get("ExpirationDate", {}).get('content'),
                'bank_name': fields.get("IssuingBank", {}).get('content')
            }            
    except Exception as ex:
        print(f"Erro ao analisar o documento: {ex}")
        return AssertionError
    