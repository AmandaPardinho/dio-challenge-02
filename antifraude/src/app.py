import streamlit as st
from service.blob_service import upload_blob
from service.credit_card_service import analize_credit_card

def configure_interface():
    st.title('Upload de Arquivo DIO - Desafio 2 - Azure - Fake Docs')
    st.write('Esse é um aplicativo para a realização do upload de arquivos de imagens para a identificação de documentos falsos.')
    uploaded_file = st.file_uploader("Escolha um arquivo", type=['png', 'jpg', 'jpeg'])

    if uploaded_file is not None:
        fileName = uploaded_file.name
        #enviar para o blob storage
        blob_url = upload_blob(uploaded_file, fileName)
        if blob_url is not None:
            st.write(f"Arquivo {fileName} enviado com sucesso para o Azure Blob Storage!")
            credit_card_info = analize_credit_card(blob_url)
            if credit_card_info and isinstance(credit_card_info, dict) and 'card_name' in credit_card_info:
                show_image_and_validation(blob_url, credit_card_info)
            else:
                st.error("Erro ao analisar o cartão de crédito.")
            #show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Erro ao enviar o arquivo {fileName} para o Azure Blob Storage!")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption='Imagem enviada', use_container_width=True)
    st.write('Resultado da validação: ')
    if credit_card_info and credit_card_info['card_name']:
        st.markdown(f"<h1 style='color:green;'>Cartão válido</h1>", unsafe_allow_html=True)
        st.write(f'Nome do titular do cartão: {credit_card_info["card_name"]}')
        st.write(f"Banco emissor: {credit_card_info['bank_name']}")
        st.write(f"Data de validade: {credit_card_info['expiration_date']}")
    else:
        st.markdown(f"<h1 style='color:red;'>Cartão inválido</h1>", unsafe_allow_html=True)
        st.write("Este cartão de crédito não é válido.")

    st.write('Informações do cartão de crédito detectadas:')
    st.write(credit_card_info)

if __name__ == '__main__':
    configure_interface() 