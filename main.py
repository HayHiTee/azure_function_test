
import os
import shutil
from pathlib import Path

from email_processing import split_file, is_this_pdf
from connectors_azure import upload_file_to_storage, download_file_from_storage
from config import azure_storage_connectors


known_suppliers = ['rb', 'fmc']

# TODO this is where the blob/name trigger comes in
blob_to_download = 'rb-sample.pdf'



def main():
    os.chdir(os.path.dirname(os.path.realpath(__file__)))

    download_file_from_storage(blob_to_download, blob_to_download, azure_storage_connectors['connection_string'], azure_storage_connectors['inbox_container'])
    supplier_name = blob_to_download.split('-')[0]

    # known supplier and pdf attachment -> split pages and upload to 'ready' storage 
    if supplier_name in known_suppliers and blob_to_download.endswith('.pdf'):
        split_file(blob_to_download)

        for file_to_upload in os.listdir('.'):
            if 'page' in file_to_upload:
                upload_file_to_storage(file_to_upload, azure_storage_connectors['connection_string'], azure_storage_connectors['ready_files_container'])
                os.remove(file_to_upload)

    # known supplier and unknown attachment format -> upload to 'unknown_format' storage
    elif supplier_name in known_suppliers:
        upload_file_to_storage(blob_to_download, azure_storage_connectors['connection_string'], azure_storage_connectors['unknown_format_container'])

    os.remove(blob_to_download)


if __name__ == "__main__":
    main()